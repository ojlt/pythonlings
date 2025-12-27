"""Progress tracking using JSON state file."""

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

STATE_FILE = ".pythonlings_state.json"


@dataclass
class ExerciseState:
    """State of a single exercise."""
    completed: bool = False
    completed_at: Optional[str] = None
    attempts: int = 0
    hints_viewed: int = 0


class ProgressTracker:
    """Track exercise completion state."""

    def __init__(self, project_root: Path):
        self.state_file = project_root / STATE_FILE
        self.state: dict[str, ExerciseState] = {}
        self._load()

    def _load(self) -> None:
        """Load state from file."""
        if self.state_file.exists():
            try:
                data = json.loads(self.state_file.read_text())
                self.state = {
                    name: ExerciseState(**state_data)
                    for name, state_data in data.items()
                }
            except (json.JSONDecodeError, TypeError):
                self.state = {}

    def _save(self) -> None:
        """Save state to file."""
        data = {name: asdict(state) for name, state in self.state.items()}
        self.state_file.write_text(json.dumps(data, indent=2))

    def _ensure_state(self, exercise_name: str) -> None:
        """Ensure state exists for an exercise."""
        if exercise_name not in self.state:
            self.state[exercise_name] = ExerciseState()

    def mark_complete(self, exercise_name: str) -> None:
        """Mark an exercise as complete."""
        self._ensure_state(exercise_name)
        self.state[exercise_name].completed = True
        self.state[exercise_name].completed_at = datetime.now().isoformat()
        self._save()

    def mark_incomplete(self, exercise_name: str) -> None:
        """Mark an exercise as incomplete (for reset)."""
        self._ensure_state(exercise_name)
        self.state[exercise_name].completed = False
        self.state[exercise_name].completed_at = None
        self._save()

    def record_attempt(self, exercise_name: str) -> None:
        """Record an attempt at an exercise."""
        self._ensure_state(exercise_name)
        self.state[exercise_name].attempts += 1
        self._save()

    def record_hint_viewed(self, exercise_name: str) -> None:
        """Record that a hint was viewed."""
        self._ensure_state(exercise_name)
        self.state[exercise_name].hints_viewed += 1
        self._save()

    def get_hints_viewed(self, exercise_name: str) -> int:
        """Get the number of hints viewed for an exercise."""
        if exercise_name not in self.state:
            return 0
        return self.state[exercise_name].hints_viewed

    def get_progress(self, total_exercises: int) -> tuple[int, int]:
        """Return (completed_count, total_count)."""
        completed = sum(1 for s in self.state.values() if s.completed)
        return completed, total_exercises

    def is_complete(self, exercise_name: str) -> bool:
        """Check if an exercise is marked complete."""
        return self.state.get(exercise_name, ExerciseState()).completed
