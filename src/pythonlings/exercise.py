"""Exercise model and related utilities."""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional


class ExerciseStatus(Enum):
    """Status of an exercise."""
    PENDING = "pending"
    DONE = "done"


@dataclass
class Exercise:
    """Represents a single exercise."""

    name: str
    path: Path
    category: str
    difficulty: str
    hints: list[str]
    description: str

    INCOMPLETE_MARKER = "# I AM NOT DONE"

    def is_complete(self) -> bool:
        """Check if the marker has been removed from the file."""
        if not self.path.exists():
            return False
        content = self.path.read_text()
        return self.INCOMPLETE_MARKER not in content

    def mark_complete(self) -> None:
        """Remove the incomplete marker from the file."""
        if not self.path.exists():
            return
        content = self.path.read_text()
        if self.INCOMPLETE_MARKER in content:
            # Remove the marker line (and any trailing newline)
            new_content = content.replace(self.INCOMPLETE_MARKER + "\n", "")
            new_content = new_content.replace(self.INCOMPLETE_MARKER, "")
            self.path.write_text(new_content)

    def get_status(self) -> ExerciseStatus:
        """Get the current status of this exercise."""
        return ExerciseStatus.DONE if self.is_complete() else ExerciseStatus.PENDING

    def get_content(self) -> str:
        """Read the exercise file content."""
        return self.path.read_text()


@dataclass
class ExerciseResult:
    """Result of running an exercise."""

    exercise: Exercise
    success: bool
    output: str
    error: Optional[str] = None
    test_count: int = 0
    passed_count: int = 0
    failed_tests: list[str] | None = None
