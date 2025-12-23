#!/usr/bin/env python3
"""
Comprehensive Test Runner for Python for Beginners Book
Runs and validates all code examples from the companion repository
"""

import subprocess
import sys
from pathlib import Path
from collections import defaultdict
import time

class TestRunner:
    def __init__(self):
        self.test_dir = Path(__file__).parent.parent  # Go up from tests/ to root
        self.results = defaultdict(lambda: {"passed": [], "failed": [], "skipped": []})
        self.total_passed = 0
        self.total_failed = 0
        self.total_skipped = 0

        # Files that require user input (will be skipped in automated testing)
        self.interactive_files = {
            "exercise-03-calculations.py",
            "01-simple-calculator.py",
            "16-input-basic.py",
            "17-simple-calculator.py",
            "exercise-03-celsius-to-fahrenheit.py",
            "exercise-04-rectangle.py",
            "exercise-05-tip-calculator.py",
            "exercise-06-even-odd.py",
            "exercise-07-can-drive.py",
            "01-guessing-game.py",
            "05-password-checker.py",
            "06-temperature-advisor.py",
            "07-even-or-odd.py",
            "13-while-loop-practical.py",
            "exercise-01-positive-negative-zero.py",
            "exercise-03-factorial.py",
            "exercise-05-password-validator.py",
            "exercise-06-letter-counter.py",
            "exercise-08-calculator-menu.py",
            "18-guessing-game.py",
            "26-calculator-main.py",
            "18-note-taking-app.py",
            "20-calculator-with-errors.py",
            "project-01-calculator.py",
            "project-02-todo-list.py",
            "project-03-guessing-game.py",
            "project-04-file-organizer.py",
        }

    def is_interactive(self, file_path):
        """Check if a file requires user input"""
        return file_path.name in self.interactive_files

    def run_file(self, file_path, timeout=5):
        """Run a single Python file and return result"""
        try:
            result = subprocess.run(
                [sys.executable, str(file_path)],
                capture_output=True,
                text=True,
                timeout=timeout
            )

            if result.returncode == 0:
                return "passed", None
            else:
                return "failed", f"Exit code {result.returncode}: {result.stderr}"

        except subprocess.TimeoutExpired:
            return "failed", "Timeout (likely waiting for input)"
        except Exception as e:
            return "failed", str(e)

    def test_chapter(self, chapter_num):
        """Test all files in a chapter"""
        chapter_dir = self.test_dir / f"chapter-{chapter_num:02d}"

        if not chapter_dir.exists():
            print(f"  ⚠️  Chapter {chapter_num} directory not found")
            return

        # Collect files from examples/ and exercises/solutions/
        py_files = []

        examples_dir = chapter_dir / "examples"
        if examples_dir.exists():
            py_files.extend(sorted(examples_dir.glob("*.py")))

        solutions_dir = chapter_dir / "exercises" / "solutions"
        if solutions_dir.exists():
            py_files.extend(sorted(solutions_dir.glob("*.py")))

        if not py_files:
            print(f"  ⚠️  No Python files found in Chapter {chapter_num}")
            return

        for py_file in py_files:
            # Skip interactive files
            if self.is_interactive(py_file):
                self.results[chapter_num]["skipped"].append(py_file.name)
                self.total_skipped += 1
                print(f"    ⊘ {py_file.name} (interactive - skipped)")
                continue

            # Run the file
            status, error = self.run_file(py_file)

            if status == "passed":
                self.results[chapter_num]["passed"].append(py_file.name)
                self.total_passed += 1
                print(f"    ✓ {py_file.name}")
            else:
                self.results[chapter_num]["failed"].append((py_file.name, error))
                self.total_failed += 1
                print(f"    ✗ {py_file.name}")
                if error:
                    print(f"      Error: {error[:100]}")

    def run_all_tests(self):
        """Run tests for all chapters"""
        print("=" * 70)
        print("Python for Beginners - Comprehensive Code Test Suite")
        print("=" * 70)
        print()

        start_time = time.time()

        for chapter_num in range(1, 11):
            print(f"📖 Chapter {chapter_num:02d}")
            self.test_chapter(chapter_num)
            print()

        elapsed_time = time.time() - start_time

        # Print summary
        print("=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        print()

        for chapter_num in range(1, 11):
            if chapter_num in self.results:
                passed = len(self.results[chapter_num]["passed"])
                failed = len(self.results[chapter_num]["failed"])
                skipped = len(self.results[chapter_num]["skipped"])
                total = passed + failed + skipped

                print(f"Chapter {chapter_num:02d}: {passed}/{total} passed, {failed} failed, {skipped} skipped")

        print()
        print("-" * 70)
        print(f"TOTAL: {self.total_passed} passed, {self.total_failed} failed, {self.total_skipped} skipped")
        print(f"Time: {elapsed_time:.2f} seconds")
        print("-" * 70)

        # Show failed tests
        if self.total_failed > 0:
            print()
            print("❌ FAILED TESTS:")
            for chapter_num, results in self.results.items():
                if results["failed"]:
                    print(f"\n  Chapter {chapter_num}:")
                    for filename, error in results["failed"]:
                        print(f"    - {filename}")
                        if error:
                            print(f"      {error[:200]}")

        # Exit code
        if self.total_failed > 0:
            print()
            print("⚠️  Some tests failed. Please review the errors above.")
            return 1
        else:
            print()
            print("✅ All non-interactive tests passed!")
            return 0


def main():
    """Main entry point"""
    runner = TestRunner()
    exit_code = runner.run_all_tests()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
