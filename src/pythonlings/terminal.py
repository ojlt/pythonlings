"""Rich console output formatting."""

from collections import defaultdict

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .exercise import Exercise, ExerciseResult

# Display names for difficulty levels
DIFFICULTY_DISPLAY = {
    "easy": ("Easy", "green"),
    "medium": ("Medium", "yellow"),
    "hard": ("Hard", "red"),
    "leetcode_easy": ("LeetCode Easy", "cyan"),
    "leetcode_medium": ("LeetCode Medium", "blue"),
    "leetcode_hard": ("LeetCode Hard", "magenta"),
}

# Order for displaying difficulty groups
DIFFICULTY_ORDER = [
    "easy", "medium", "hard",
    "leetcode_easy", "leetcode_medium", "leetcode_hard"
]


def create_console() -> Console:
    """Create a Rich console instance."""
    return Console()


def display_result(console: Console, result: ExerciseResult, verbose: bool = False) -> None:
    """Display exercise test result."""
    if result.success:
        console.print(Panel(
            f"[bold green]All tests passed![/]\n\n"
            f"Tests: {result.passed_count}/{result.test_count}",
            title=f"[green]{result.exercise.name}[/]",
            border_style="green"
        ))

        if not result.exercise.is_complete():
            console.print(
                "\n[yellow]Remove the '# I AM NOT DONE' marker "
                "to mark this exercise as complete.[/]"
            )
    else:
        # Build concise failure message
        failed_list = ""
        if result.failed_tests:
            failed_list = "\n\n[bold]Failed:[/]\n" + "\n".join(
                f"  [red]✗[/] {test}" for test in result.failed_tests
            )

        console.print(Panel(
            f"[bold red]Tests failed[/]\n\n"
            f"Tests: {result.passed_count}/{result.test_count}"
            f"{failed_list}",
            title=f"[red]{result.exercise.name}[/]",
            border_style="red"
        ))

        if verbose:
            # Show full output only in verbose mode
            if result.output:
                console.print("\n[bold]Test Output:[/]")
                console.print(result.output)
            if result.error:
                console.print("\n[bold red]Errors:[/]")
                console.print(result.error)
        else:
            console.print(
                f"\nRun 'pythonlings run {result.exercise.name}' "
                "for full error details."
            )


def display_hint(console: Console, exercise: Exercise, hint_index: int) -> None:
    """Display a hint for the exercise."""
    if hint_index < len(exercise.hints):
        console.print(Panel(
            exercise.hints[hint_index],
            title=f"[yellow]Hint {hint_index + 1}/{len(exercise.hints)}[/]",
            border_style="yellow"
        ))
        if hint_index < len(exercise.hints) - 1:
            console.print(
                "\nRun 'pythonlings hint' again for the next hint."
            )
    else:
        console.print("[yellow]No more hints available![/]")


def display_progress(console: Console, completed: int, total: int, bar_width: int = 30) -> str:
    """Generate a progress bar string."""
    percentage = (completed / total * 100) if total > 0 else 0
    filled = int(bar_width * completed / total) if total > 0 else 0
    bar = "█" * filled + "░" * (bar_width - filled)
    return f"[{bar}] {completed}/{total} ({percentage:.0f}%)"


def display_exercise_list(
    console: Console,
    exercises: list[Exercise],
    completed: int,
    total: int
) -> None:
    """Display exercises grouped by difficulty in compact format."""
    # Group exercises by difficulty
    groups = defaultdict(list)
    for ex in exercises:
        groups[ex.difficulty].append(ex)

    # Display each group
    for difficulty in DIFFICULTY_ORDER:
        if difficulty not in groups:
            continue

        group_exercises = groups[difficulty]
        group_completed = sum(1 for ex in group_exercises if ex.is_complete())
        group_total = len(group_exercises)

        # Get display name and color
        display_name, color = DIFFICULTY_DISPLAY.get(difficulty, (difficulty.title(), "white"))

        # Section header with compact progress
        console.print(f"\n[bold {color}]{display_name}[/] ({group_completed}/{group_total})")

        # Compact exercise list - multiple per line
        term_width = console.width or 80
        col_width = 38
        cols = max(1, term_width // col_width)

        for i in range(0, len(group_exercises), cols):
            row_exercises = group_exercises[i:i + cols]
            parts = []
            for ex in row_exercises:
                status = "[green]✓[/]" if ex.is_complete() else "[dim]○[/]"
                # Truncate and pad name to fixed width for alignment
                name = ex.name[:30] if len(ex.name) > 30 else ex.name
                name_padded = name.ljust(32)
                parts.append(f"{status} [cyan]{name_padded}[/]")
            console.print("  " + "".join(parts))

    # Overall progress
    console.print(f"\n[bold]Total:[/] {display_progress(console, completed, total)}")


def display_welcome(console: Console) -> None:
    """Display welcome message."""
    console.print(Panel(
        "[bold]Welcome to Pythonlings![/]\n\n"
        "Learn Python by solving exercises - inspired by rustlings!\n\n"
        "Commands:\n"
        "  [cyan]pythonlings run[/]     - Run the next pending exercise\n"
        "  [cyan]pythonlings watch[/]   - Watch mode (auto-run on save)\n"
        "  [cyan]pythonlings hint[/]    - Get a hint\n"
        "  [cyan]pythonlings list[/]    - List all exercises\n"
        "  [cyan]pythonlings reset[/]   - Reset an exercise",
        title="[bold blue]Pythonlings[/]",
        border_style="blue"
    ))


def display_watch_header(
    console: Console,
    exercise: Exercise,
    completed: int,
    total: int,
    exercises: list[Exercise] | None = None
) -> None:
    """Display watch mode header with grouped progress."""
    # Get difficulty display info
    display_name, color = DIFFICULTY_DISPLAY.get(
        exercise.difficulty, (exercise.difficulty.title(), "white")
    )

    # Build progress info
    progress_lines = []

    if exercises:
        # Group progress
        groups = defaultdict(list)
        for ex in exercises:
            groups[ex.difficulty].append(ex)

        for difficulty in DIFFICULTY_ORDER:
            if difficulty not in groups:
                continue
            group_exercises = groups[difficulty]
            group_completed = sum(1 for ex in group_exercises if ex.is_complete())
            group_total = len(group_exercises)
            diff_name, diff_color = DIFFICULTY_DISPLAY.get(difficulty, (difficulty.title(), "white"))

            if difficulty == exercise.difficulty:
                # Highlight current group
                progress_lines.append(
                    f"[bold {diff_color}]► {diff_name}: {group_completed}/{group_total}[/]"
                )
            else:
                progress_lines.append(
                    f"[dim]  {diff_name}: {group_completed}/{group_total}[/]"
                )

    progress_text = "\n".join(progress_lines) if progress_lines else f"{completed}/{total}"

    console.print(Panel(
        f"[bold]Exercise:[/] {exercise.name}\n"
        f"[bold]Difficulty:[/] [{color}]{display_name}[/]\n"
        f"[bold]Category:[/] {exercise.category}\n"
        f"[bold]Status:[/] {'[green]Done[/]' if exercise.is_complete() else '[yellow]Pending[/]'}\n\n"
        f"[bold]Progress:[/]\n{progress_text}",
        title="[bold blue]Watch Mode[/]",
        border_style="blue"
    ))
