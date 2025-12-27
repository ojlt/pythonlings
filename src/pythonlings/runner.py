"""Test runner using pytest."""

import re
import subprocess
import sys
from pathlib import Path

from .exercise import Exercise, ExerciseResult


class ExerciseRunner:
    """Runs exercises using pytest."""

    def run(self, exercise: Exercise) -> ExerciseResult:
        """Execute the exercise tests and return the result."""
        if not exercise.path.exists():
            return ExerciseResult(
                exercise=exercise,
                success=False,
                output="",
                error=f"Exercise file not found: {exercise.path}",
                test_count=0,
                passed_count=0,
            )

        result = subprocess.run(
            [
                sys.executable, "-m", "pytest",
                str(exercise.path),
                "-v", "--tb=short", "--no-header", "-q"
            ],
            capture_output=True,
            text=True,
            cwd=exercise.path.parent.parent.parent,
        )

        success = result.returncode == 0
        output = result.stdout
        error = result.stderr if result.returncode != 0 else None

        test_count, passed_count, failed_tests = self._parse_pytest_output(output)

        return ExerciseResult(
            exercise=exercise,
            success=success,
            output=output,
            error=error,
            test_count=test_count,
            passed_count=passed_count,
            failed_tests=failed_tests,
        )

    def _parse_pytest_output(self, output: str) -> tuple[int, int, list[str]]:
        """Extract test counts and failed test names from pytest output."""
        passed_match = re.search(r"(\d+) passed", output)
        failed_match = re.search(r"(\d+) failed", output)

        passed = int(passed_match.group(1)) if passed_match else 0
        failed = int(failed_match.group(1)) if failed_match else 0

        # Extract failed test names (format: "FAILED file.py::test_name - ...")
        failed_tests = re.findall(r"FAILED [^:]+::(\w+)", output)

        return passed + failed, passed, failed_tests

    def run_all(self, exercises: list[Exercise]) -> list[ExerciseResult]:
        """Run all exercises and return results."""
        results = []
        for exercise in exercises:
            result = self.run(exercise)
            results.append(result)
        return results
