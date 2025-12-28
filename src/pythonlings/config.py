"""Configuration loading from exercises.toml."""

import shutil
import tomllib
from pathlib import Path

from .exercise import Exercise


def find_project_root() -> Path:
    """Find the project root by looking for exercises.toml."""
    current = Path.cwd()

    while current != current.parent:
        if (current / "exercises.toml").exists():
            return current
        current = current.parent

    # Default to current directory
    return Path.cwd()


def load_exercises(project_root: Path | None = None) -> list[Exercise]:
    """Load exercises from exercises.toml configuration."""
    if project_root is None:
        project_root = find_project_root()

    config_path = project_root / "exercises.toml"

    if not config_path.exists():
        return []

    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    exercises = []

    for exercise_config in config.get("exercises", []):
        path = project_root / exercise_config["path"]
        exercise = Exercise(
            name=exercise_config["name"],
            path=path,
            category=exercise_config["category"],
            difficulty=exercise_config.get("difficulty", "easy"),
            hints=exercise_config.get("hints", []),
            description=exercise_config.get("description", ""),
        )
        exercises.append(exercise)

    return exercises


def get_exercise_by_name(name: str, project_root: Path | None = None) -> Exercise | None:
    """Get a specific exercise by name."""
    exercises = load_exercises(project_root)
    for exercise in exercises:
        if exercise.name == name:
            return exercise
    return None


def get_next_pending_exercise(project_root: Path | None = None) -> Exercise | None:
    """Get the next pending (incomplete) exercise."""
    exercises = load_exercises(project_root)
    for exercise in exercises:
        if not exercise.is_complete():
            return exercise
    return None


def init_exercises(project_root: Path | None = None) -> int:
    """Initialize exercises from templates. Only copies files that don't exist.

    Returns the number of files copied (0 if already initialized).
    """
    if project_root is None:
        project_root = find_project_root()

    templates_dir = project_root / "templates"
    exercises_dir = project_root / "exercises"

    if not templates_dir.exists():
        return 0

    copied = 0
    for template_file in templates_dir.rglob("*"):
        if template_file.is_file():
            relative_path = template_file.relative_to(templates_dir)
            target_file = exercises_dir / relative_path

            # Only copy if target doesn't exist (preserve user's work)
            if not target_file.exists():
                target_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(template_file, target_file)
                copied += 1

    return copied
