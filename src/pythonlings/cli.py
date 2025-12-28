"""CLI application using Typer."""

import shutil
from pathlib import Path
from typing import Optional

import typer

from .config import find_project_root, get_exercise_by_name, init_exercises, load_exercises
from .state import ProgressTracker
from .terminal import create_console
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
        template_path = templates_dir / exercise.path.relative_to(root / "exercises")
        if not template_path.exists():
            console.print(f"[yellow]Warning: No template for '{exercise.name}'[/]")
            return False
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


@app.callback(invoke_without_command=True)
def main_callback(ctx: typer.Context) -> None:
    """Main callback - start watch mode if no command given."""
    if ctx.invoked_subcommand is None:
        root = get_project_root()
        watch_mode = WatchMode(root)
        watch_mode.start()


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
