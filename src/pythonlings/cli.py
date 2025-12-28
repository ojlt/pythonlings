"""CLI application using Typer."""

import shutil
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from .config import find_project_root, get_exercise_by_name, get_next_pending_exercise, init_exercises, load_exercises
from .runner import ExerciseRunner
from .state import ProgressTracker
from .terminal import (
    create_console,
    display_exercise_list,
    display_hint,
    display_result,
    display_welcome,
)
from .watcher import WatchMode

app = typer.Typer(
    name="pythonlings",
    help="Learn Python by solving exercises - inspired by rustlings!",
    add_completion=False,
)


def get_project_root() -> Path:
    """Get the project root or exit with error."""
    root = find_project_root()
    if not (root / "exercises.toml").exists():
        console = create_console()
        console.print(
            "[red]Error: exercises.toml not found.[/]\n"
            "Make sure you're in a pythonlings project directory."
        )
        raise typer.Exit(1)

    # Initialize exercises from templates (copies new/missing files only)
    copied = init_exercises(root)
    if copied > 0:
        console = create_console()
        console.print(f"[green]Initialized {copied} exercise file(s) from templates.[/]\n")

    return root


@app.command()
def run(
    name: Optional[str] = typer.Argument(
        None,
        help="Exercise name to run (defaults to next pending)"
    )
) -> None:
    """Run a specific exercise or the next pending exercise."""
    console = create_console()
    root = get_project_root()

    if name:
        exercise = get_exercise_by_name(name, root)
        if not exercise:
            console.print(f"[red]Exercise '{name}' not found.[/]")
            raise typer.Exit(1)
    else:
        exercise = get_next_pending_exercise(root)
        if not exercise:
            console.print("[green]All exercises completed! Great job![/]")
            return

    console.print(f"[bold]Running:[/] {exercise.name}\n")

    runner = ExerciseRunner()
    tracker = ProgressTracker(root)

    result = runner.run(exercise)
    tracker.record_attempt(exercise.name)
    display_result(console, result, verbose=True)

    if result.success and exercise.is_complete():
        tracker.mark_complete(exercise.name)


@app.command()
def watch() -> None:
    """Watch for file changes and auto-run exercises."""
    root = get_project_root()
    watch_mode = WatchMode(root)
    watch_mode.start()


@app.command()
def hint(
    name: Optional[str] = typer.Argument(
        None,
        help="Exercise name (defaults to next pending)"
    )
) -> None:
    """Display hints for an exercise."""
    console = create_console()
    root = get_project_root()

    if name:
        exercise = get_exercise_by_name(name, root)
        if not exercise:
            console.print(f"[red]Exercise '{name}' not found.[/]")
            raise typer.Exit(1)
    else:
        exercise = get_next_pending_exercise(root)
        if not exercise:
            console.print("[green]All exercises completed![/]")
            return

    tracker = ProgressTracker(root)
    hint_index = tracker.get_hints_viewed(exercise.name)

    if hint_index >= len(exercise.hints):
        console.print(f"[yellow]No more hints for '{exercise.name}'![/]")
        return

    display_hint(console, exercise, hint_index)
    tracker.record_hint_viewed(exercise.name)


@app.command("list")
def list_exercises() -> None:
    """List all exercises with their status."""
    console = create_console()
    root = get_project_root()

    exercises = load_exercises(root)
    if not exercises:
        console.print("[yellow]No exercises found.[/]")
        return

    completed = sum(1 for ex in exercises if ex.is_complete())
    display_exercise_list(console, exercises, completed, len(exercises))


@app.command()
def reset(
    name: Optional[str] = typer.Argument(
        None,
        help="Exercise name to reset (omit for --all)"
    ),
    all_exercises: bool = typer.Option(
        False,
        "--all",
        "-a",
        help="Reset all exercises"
    ),
) -> None:
    """Reset an exercise to its original state."""
    console = create_console()
    root = get_project_root()
    tracker = ProgressTracker(root)
    templates_dir = root / "templates"

    def reset_exercise(exercise) -> bool:
        """Reset a single exercise. Returns True if successful."""
        # Find template file
        template_path = templates_dir / exercise.path.relative_to(root / "exercises")
        if not template_path.exists():
            console.print(f"[yellow]Warning: No template for '{exercise.name}'[/]")
            return False
        # Copy template to exercise
        shutil.copy(template_path, exercise.path)
        tracker.mark_incomplete(exercise.name)
        return True

    if all_exercises:
        exercises = load_exercises(root)
        reset_count = sum(1 for ex in exercises if reset_exercise(ex))
        console.print(f"[green]Reset {reset_count}/{len(exercises)} exercises to original state.[/]")
        return

    if not name:
        console.print("[red]Provide an exercise name or use --all.[/]")
        raise typer.Exit(1)

    exercise = get_exercise_by_name(name, root)
    if not exercise:
        console.print(f"[red]Exercise '{name}' not found.[/]")
        raise typer.Exit(1)

    if reset_exercise(exercise):
        console.print(f"[green]Reset '{name}' to original state.[/]")
    else:
        raise typer.Exit(1)


@app.command()
def verify() -> None:
    """Verify all exercises pass."""
    console = create_console()
    root = get_project_root()

    exercises = load_exercises(root)
    if not exercises:
        console.print("[yellow]No exercises found.[/]")
        return

    runner = ExerciseRunner()
    results = runner.run_all(exercises)

    passed = sum(1 for r in results if r.success)
    total = len(results)

    console.print(f"\n[bold]Results: {passed}/{total} exercises pass[/]\n")

    for result in results:
        status = "[green]PASS[/]" if result.success else "[red]FAIL[/]"
        console.print(f"  {status} {result.exercise.name}")

    if passed == total:
        console.print("\n[bold green]All exercises pass![/]")
    else:
        console.print(
            f"\n[yellow]{total - passed} exercise(s) need attention.[/]"
        )


@app.callback(invoke_without_command=True)
def main_callback(ctx: typer.Context) -> None:
    """Main callback - start watch mode if no command given (like rustlings)."""
    if ctx.invoked_subcommand is None:
        root = get_project_root()
        watch_mode = WatchMode(root)
        watch_mode.start()


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
