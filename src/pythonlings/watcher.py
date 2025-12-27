"""File watching using watchdog."""

import select
import sys
import termios
import time
import tty
from pathlib import Path
from threading import Lock

from watchdog.observers.polling import PollingObserver

from .config import load_exercises
from .exercise import Exercise
from .runner import ExerciseRunner
from .state import ProgressTracker
from .terminal import (
    create_console,
    display_result,
    display_watch_header,
    DIFFICULTY_DISPLAY,
    DIFFICULTY_ORDER,
)


class WatchMode:
    """Watch mode for auto-running exercises on file changes."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.exercises_dir = project_root / "exercises"
        self.console = create_console()
        self.runner = ExerciseRunner()
        self.tracker = ProgressTracker(project_root)
        self.exercises: list[Exercise] = []
        self.current_index: int = 0
        self.last_result = None
        self.lock = Lock()
        self._last_modified: float = 0

    def _get_current_exercise(self) -> Exercise:
        """Get the current exercise."""
        return self.exercises[self.current_index]

    def _count_completed(self) -> int:
        """Count completed exercises."""
        return sum(1 for ex in self.exercises if ex.is_complete())

    def _refresh_display(self, show_result: bool = True) -> None:
        """Refresh the screen with current exercise info."""
        exercise = self._get_current_exercise()
        completed = self._count_completed()

        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()

        display_watch_header(self.console, exercise, completed, len(self.exercises), self.exercises)
        self.console.print()

        # Show exercise status
        if exercise.is_complete():
            self.console.print("[bold green]This exercise is complete![/]\n")
        else:
            self.console.print(f"[cyan]Edit:[/] {exercise.path}\n")

        # Show last test result if available and for current exercise
        if show_result and self.last_result and self.last_result.exercise.name == exercise.name:
            display_result(self.console, self.last_result)
            self.console.print()

        # Navigation help
        self.console.print("n=next  p=prev  l=list  r=run  q=quit")

    def _render_list(self, browse_index: int) -> None:
        """Render the exercise list with current browse position."""
        from collections import defaultdict

        # Move cursor home without clearing (prevents flash)
        sys.stdout.write('\033[H')
        sys.stdout.flush()

        self.console.print("[bold]Exercises[/] [dim](j/k to browse, Enter to select, q to cancel)[/]")

        # Group exercises by difficulty
        groups = defaultdict(list)
        for i, ex in enumerate(self.exercises):
            groups[ex.difficulty].append((i, ex))

        # Display each group in compact format
        term_width = self.console.width or 80
        col_width = 38
        cols = max(1, term_width // col_width)

        for difficulty in DIFFICULTY_ORDER:
            if difficulty not in groups:
                continue

            group_exercises = groups[difficulty]
            group_completed = sum(1 for _, ex in group_exercises if ex.is_complete())
            group_total = len(group_exercises)

            display_name, color = DIFFICULTY_DISPLAY.get(difficulty, (difficulty.title(), "white"))
            self.console.print(f"\n[bold {color}]{display_name}[/] ({group_completed}/{group_total})")

            # Compact multi-column display
            for row_start in range(0, len(group_exercises), cols):
                row = group_exercises[row_start:row_start + cols]
                parts = []
                for i, ex in row:
                    is_selected = (i == browse_index)
                    status = "[green]✓[/]" if ex.is_complete() else "[dim]○[/]"
                    name = ex.name[:28] if len(ex.name) > 28 else ex.name
                    if is_selected:
                        parts.append(f"[bold reverse]  {status} {name.ljust(28)}[/]")
                    else:
                        parts.append(f"  {status} [cyan]{name.ljust(28)}[/]")
                self.console.print("  " + "".join(parts))

    def _show_list(self) -> None:
        """Interactive list browser."""
        browse_index = self.current_index
        needs_redraw = True

        # Hide cursor and clear screen once at start
        sys.stdout.write('\033[?25l\033[2J')
        sys.stdout.flush()

        try:
            while True:
                if needs_redraw:
                    self._render_list(browse_index)
                    needs_redraw = False

                # Wait for key input (blocking with timeout)
                if select.select([sys.stdin], [], [], 0.1)[0]:
                    key = sys.stdin.read(1)

                    # Handle arrow keys (escape sequences)
                    if key == '\x1b':
                        # Read the rest of escape sequence
                        if select.select([sys.stdin], [], [], 0.05)[0]:
                            seq = sys.stdin.read(2)
                            if seq == '[A':  # Up arrow
                                key = 'k'
                            elif seq == '[B':  # Down arrow
                                key = 'j'
                            else:
                                # Escape key alone - cancel
                                break

                    old_index = browse_index

                    if key in ('j', 'n'):  # Down/next
                        browse_index = min(browse_index + 1, len(self.exercises) - 1)
                    elif key in ('k', 'p'):  # Up/prev
                        browse_index = max(browse_index - 1, 0)
                    elif key == '\r' or key == '\n':  # Enter - select
                        self.current_index = browse_index
                        self.last_result = None
                        break
                    elif key == 'q':  # q - cancel
                        break

                    # Only redraw if index changed
                    if browse_index != old_index:
                        needs_redraw = True
        finally:
            # Restore cursor
            sys.stdout.write('\033[?25h')
            sys.stdout.flush()

        self._refresh_display(show_result=False)

    def _go_next(self) -> None:
        """Move to next exercise."""
        if self.current_index < len(self.exercises) - 1:
            self.current_index += 1
            self.last_result = None
            self._refresh_display(show_result=False)

    def _go_prev(self) -> None:
        """Move to previous exercise."""
        if self.current_index > 0:
            self.current_index -= 1
            self.last_result = None
            self._refresh_display(show_result=False)

    def _run_current(self) -> None:
        """Run the current exercise."""
        exercise = self._get_current_exercise()
        self.last_result = self.runner.run(exercise)
        self.tracker.record_attempt(exercise.name)

        if self.last_result.success:
            exercise.mark_complete()
            self.tracker.mark_complete(exercise.name)

        self._refresh_display()

    def _handle_file_change(self, path: Path) -> None:
        """Handle a file change event."""
        with self.lock:
            current_time = time.time()
            if current_time - self._last_modified < 0.5:
                return
            self._last_modified = current_time

            if path.suffix != ".py":
                return

            # Check if this file matches the current exercise
            exercise = self._get_current_exercise()
            if path != exercise.path.resolve():
                return

            # Run the exercise
            self._run_current()

    def start(self) -> None:
        """Start watching for file changes."""
        self.exercises = load_exercises(self.project_root)
        if not self.exercises:
            self.console.print(
                "[red]No exercises found. "
                "Make sure exercises.toml exists.[/]"
            )
            return

        # Find first incomplete exercise
        self.current_index = 0
        for i, ex in enumerate(self.exercises):
            if not ex.is_complete():
                self.current_index = i
                break

        # Set up file watcher
        from watchdog.events import FileSystemEventHandler

        class Handler(FileSystemEventHandler):
            def __init__(handler_self, watch_mode):
                handler_self.watch_mode = watch_mode

            def on_modified(handler_self, event):
                if not event.is_directory:
                    handler_self.watch_mode._handle_file_change(
                        Path(event.src_path).resolve()
                    )

            def on_created(handler_self, event):
                if not event.is_directory:
                    handler_self.watch_mode._handle_file_change(
                        Path(event.src_path).resolve()
                    )

            def on_moved(handler_self, event):
                if not event.is_directory:
                    handler_self.watch_mode._handle_file_change(
                        Path(event.dest_path).resolve()
                    )

        observer = PollingObserver()
        observer.schedule(Handler(self), str(self.exercises_dir), recursive=True)
        observer.start()

        # Save terminal settings
        old_settings = termios.tcgetattr(sys.stdin)

        try:
            # Switch to alternate screen and raw mode
            sys.stdout.write('\033[?1049h')
            sys.stdout.flush()
            tty.setcbreak(sys.stdin.fileno())

            self._refresh_display(show_result=False)

            while True:
                # Check for keyboard input (non-blocking)
                if select.select([sys.stdin], [], [], 0.1)[0]:
                    key = sys.stdin.read(1)

                    if key == 'q':
                        break
                    elif key == 'n':
                        self._go_next()
                    elif key == 'p':
                        self._go_prev()
                    elif key == 'l':
                        self._show_list()
                    elif key == 'r':
                        self._run_current()

        except KeyboardInterrupt:
            pass
        finally:
            # Restore terminal
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            sys.stdout.write('\033[?1049l')
            sys.stdout.flush()
            self.console.print("[yellow]Stopped watch mode.[/]")
            observer.stop()
            observer.join()
