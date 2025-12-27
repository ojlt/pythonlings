"""Rich console output formatting."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .exercise import Exercise, ExerciseResult


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


def display_progress(console: Console, completed: int, total: int) -> None:
    """Display overall progress."""
    percentage = (completed / total * 100) if total > 0 else 0
    bar_width = 30
    filled = int(bar_width * completed / total) if total > 0 else 0
    bar = "█" * filled + "░" * (bar_width - filled)
    console.print(f"\nProgress: [{bar}] {completed}/{total} ({percentage:.0f}%)")


def display_exercise_list(
    console: Console,
    exercises: list[Exercise],
    completed: int,
    total: int
) -> None:
    """Display table of all exercises."""
    table = Table(title="Exercises")
    table.add_column("#", width=4)
    table.add_column("Name", style="cyan")
    table.add_column("Category", style="magenta")
    table.add_column("Status", justify="center")

    for i, ex in enumerate(exercises, 1):
        status = "[green]✓ Done[/]" if ex.is_complete() else "[yellow]○ Pending[/]"
        table.add_row(str(i), ex.name, ex.category, status)

    console.print(table)
    display_progress(console, completed, total)


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


def display_watch_header(console: Console, exercise: Exercise, completed: int, total: int) -> None:
    """Display watch mode header."""
    console.print(Panel(
        f"[bold]Current exercise:[/] {exercise.name}\n"
        f"[bold]Category:[/] {exercise.category}\n"
        f"[bold]Status:[/] {'[green]Done[/]' if exercise.is_complete() else '[yellow]Pending[/]'}\n"
        f"[bold]Progress:[/] {completed}/{total} exercises completed",
        title="[bold blue]Watch Mode[/]",
        border_style="blue"
    ))
