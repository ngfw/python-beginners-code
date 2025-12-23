#!/usr/bin/env python3
"""
Reorganize Python code files from test-code/ into companion-code/ structure.
"""

import os
import shutil
import re
from pathlib import Path
from typing import List, Dict, Tuple

# Base paths
TEST_CODE_DIR = Path("/home/user/kdp_python-for-beginners/test-code")
COMPANION_CODE_DIR = Path("/home/user/kdp_python-for-beginners/companion-code")

# Statistics
stats = {
    "examples_copied": {},
    "solutions_copied": {},
    "starters_created": {},
    "errors": []
}


def get_exercise_number(filename: str) -> str:
    """Extract exercise number from filename like 'exercise-01-name.py' -> '01'"""
    match = re.search(r'exercise-(\d+)', filename)
    return match.group(1) if match else None


def create_starter_template(solution_path: Path, starter_path: Path) -> bool:
    """
    Create a starter template from a solution file.
    Removes solution code and adds TODO comments.
    """
    try:
        with open(solution_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse the file to extract components
        lines = content.split('\n')

        # Find shebang line
        shebang = ""
        start_idx = 0
        if lines and lines[0].startswith('#!'):
            shebang = lines[0] + '\n'
            start_idx = 1

        # Find docstring
        docstring_start = None
        docstring_end = None
        in_docstring = False
        triple_quote_style = None

        for i in range(start_idx, len(lines)):
            line = lines[i].strip()
            if not in_docstring:
                if line.startswith('"""') or line.startswith("'''"):
                    triple_quote_style = '"""' if line.startswith('"""') else "'''"
                    docstring_start = i
                    in_docstring = True
                    if line.count(triple_quote_style) >= 2:  # Single-line docstring
                        docstring_end = i
                        break
            else:
                if triple_quote_style in line:
                    docstring_end = i
                    break

        # Extract original docstring
        original_docstring = ""
        code_start_idx = start_idx
        if docstring_start is not None and docstring_end is not None:
            original_docstring = '\n'.join(lines[docstring_start:docstring_end + 1])
            code_start_idx = docstring_end + 1

        # Create enhanced docstring
        enhanced_docstring = original_docstring
        if original_docstring:
            # Remove closing quotes
            enhanced_docstring = original_docstring.rstrip()
            if enhanced_docstring.endswith('"""') or enhanced_docstring.endswith("'''"):
                quote_style = '"""' if enhanced_docstring.endswith('"""') else "'''"
                enhanced_docstring = enhanced_docstring[:-3]

            # Add instructions
            enhanced_docstring += '\n\nTODO: Complete the exercises below\n"""'

        # Extract main code content (everything after docstring)
        code_content = '\n'.join(lines[code_start_idx:]).strip()

        # Create starter template
        starter_content = []

        if shebang:
            starter_content.append(shebang)

        if enhanced_docstring:
            starter_content.append(enhanced_docstring)
            starter_content.append("")

        # Process the code to create starter template
        # Look for function definitions and replace their bodies with TODO
        code_lines = code_content.split('\n')
        i = 0
        while i < len(code_lines):
            line = code_lines[i]
            stripped = line.strip()

            # Check if this is a function definition
            if stripped.startswith('def '):
                # Add the function definition
                starter_content.append(line)
                i += 1

                # Find the indentation level
                indent = len(line) - len(line.lstrip())
                func_indent = ' ' * (indent + 4)

                # Skip the original function body and add TODO
                added_todo = False
                while i < len(code_lines):
                    next_line = code_lines[i]
                    next_stripped = next_line.strip()

                    # Check if we're still in the function body
                    if next_stripped and not next_line.startswith(' ' * (indent + 1)) and not next_line.startswith('\t'):
                        # We've exited the function
                        break

                    # Skip function body lines, but preserve docstrings
                    if not added_todo:
                        if next_stripped.startswith('"""') or next_stripped.startswith("'''"):
                            # This is a function docstring, keep it
                            starter_content.append(next_line)
                            quote = '"""' if next_stripped.startswith('"""') else "'''"
                            if next_stripped.count(quote) < 2:
                                # Multi-line docstring
                                i += 1
                                while i < len(code_lines):
                                    starter_content.append(code_lines[i])
                                    if quote in code_lines[i]:
                                        break
                                    i += 1

                        # Add TODO placeholder
                        starter_content.append(f"{func_indent}# TODO: Your code here")
                        starter_content.append(f"{func_indent}pass")
                        starter_content.append("")
                        added_todo = True

                    i += 1

                    if i < len(code_lines) and not code_lines[i].startswith(' ' * (indent + 1)):
                        break

                continue

            # Check if this is a class definition
            elif stripped.startswith('class '):
                starter_content.append(line)
                starter_content.append(line[:len(line) - len(line.lstrip())] + "    # TODO: Your code here")
                starter_content.append(line[:len(line) - len(line.lstrip())] + "    pass")
                starter_content.append("")

                # Skip class body
                indent = len(line) - len(line.lstrip())
                i += 1
                while i < len(code_lines) and (not code_lines[i].strip() or code_lines[i].startswith(' ' * (indent + 1))):
                    i += 1
                continue

            # Check if this is a comment that looks like a main guard
            elif 'if __name__' in stripped:
                starter_content.append("")
                starter_content.append("# Test your code")
                starter_content.append(line)
                i += 1

                # Process the if __name__ block
                indent = len(line) - len(line.lstrip())
                block_indent = ' ' * (indent + 4)

                # Look for print statements or function calls in the block
                test_cases = []
                while i < len(code_lines):
                    next_line = code_lines[i]
                    if next_line.strip() and not next_line.startswith(' ' * (indent + 1)):
                        break
                    if 'print(' in next_line:
                        # Convert to TODO comment
                        test_cases.append(f"{block_indent}# TODO: Add test cases")
                        test_cases.append(next_line)
                        i += 1
                        break
                    i += 1

                if test_cases:
                    starter_content.extend(test_cases)
                else:
                    starter_content.append(f"{block_indent}# TODO: Add test cases")
                    starter_content.append(f"{block_indent}pass")

                continue

            # Check if this is a standalone print statement (test case)
            elif stripped.startswith('print('):
                if not starter_content or starter_content[-1] != "":
                    starter_content.append("")
                starter_content.append("# Test cases")
                starter_content.append(f"# TODO: Uncomment and complete")
                starter_content.append(f"# {line}")
                i += 1

                # Collect consecutive print statements
                while i < len(code_lines) and code_lines[i].strip().startswith('print('):
                    starter_content.append(f"# {code_lines[i]}")
                    i += 1
                continue

            # Skip empty lines between functions
            elif not stripped:
                if starter_content and starter_content[-1] != "":
                    starter_content.append("")
                i += 1
                continue

            # Keep comments and other top-level code
            else:
                starter_content.append(line)
                i += 1

        # Write the starter template
        with open(starter_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(starter_content))

        # Preserve executable permissions
        if os.access(solution_path, os.X_OK):
            os.chmod(starter_path, 0o755)

        return True

    except Exception as e:
        stats["errors"].append(f"Error creating starter for {solution_path}: {str(e)}")
        return False


def process_chapter(chapter_num: str) -> Tuple[int, int, int]:
    """
    Process a single chapter: copy examples, solutions, and create starters.
    Returns: (examples_copied, solutions_copied, starters_created)
    """
    chapter_name = f"chapter-{chapter_num}"
    source_dir = TEST_CODE_DIR / chapter_name
    target_dir = COMPANION_CODE_DIR / chapter_name

    if not source_dir.exists():
        stats["errors"].append(f"Source directory not found: {source_dir}")
        return (0, 0, 0)

    # Create target directories if they don't exist
    examples_dir = target_dir / "examples"
    exercises_dir = target_dir / "exercises"
    solutions_dir = exercises_dir / "solutions"

    examples_dir.mkdir(parents=True, exist_ok=True)
    exercises_dir.mkdir(parents=True, exist_ok=True)
    solutions_dir.mkdir(parents=True, exist_ok=True)

    examples_count = 0
    solutions_count = 0
    starters_count = 0

    # Process all .py files in the source directory
    py_files = sorted(source_dir.glob("*.py"))

    for py_file in py_files:
        filename = py_file.name

        # Determine if this is an exercise file
        if filename.startswith("exercise-"):
            # Copy to solutions directory
            solution_dest = solutions_dir / filename
            shutil.copy2(py_file, solution_dest)
            solutions_count += 1

            # Create starter template
            exercise_num = get_exercise_number(filename)
            if exercise_num:
                starter_name = f"exercise-{exercise_num}.py"
                starter_dest = exercises_dir / starter_name

                if create_starter_template(py_file, starter_dest):
                    starters_count += 1

        else:
            # This is an example file, copy to examples directory
            example_dest = examples_dir / filename
            shutil.copy2(py_file, example_dest)
            examples_count += 1

    return (examples_count, solutions_count, starters_count)


def main():
    """Main reorganization function."""
    print("=" * 70)
    print("Python Code Reorganization")
    print("=" * 70)
    print()

    # Process each chapter
    for chapter_num in [f"{i:02d}" for i in range(1, 11)]:
        print(f"Processing Chapter {chapter_num}...", end=" ")

        examples, solutions, starters = process_chapter(chapter_num)

        stats["examples_copied"][chapter_num] = examples
        stats["solutions_copied"][chapter_num] = solutions
        stats["starters_created"][chapter_num] = starters

        print(f"✓ (Examples: {examples}, Solutions: {solutions}, Starters: {starters})")

    print()
    print("=" * 70)
    print("Summary Report")
    print("=" * 70)
    print()

    # Summary statistics
    total_examples = sum(stats["examples_copied"].values())
    total_solutions = sum(stats["solutions_copied"].values())
    total_starters = sum(stats["starters_created"].values())

    print(f"Total Example Files Copied:       {total_examples}")
    print(f"Total Solution Files Copied:      {total_solutions}")
    print(f"Total Starter Templates Created:  {total_starters}")
    print(f"Total Files Processed:            {total_examples + total_solutions}")
    print()

    # Per-chapter breakdown
    print("Per-Chapter Breakdown:")
    print("-" * 70)
    print(f"{'Chapter':<15} {'Examples':<15} {'Solutions':<15} {'Starters':<15}")
    print("-" * 70)

    for chapter_num in [f"{i:02d}" for i in range(1, 11)]:
        examples = stats["examples_copied"].get(chapter_num, 0)
        solutions = stats["solutions_copied"].get(chapter_num, 0)
        starters = stats["starters_created"].get(chapter_num, 0)
        print(f"Chapter {chapter_num:<7} {examples:<15} {solutions:<15} {starters:<15}")

    print("-" * 70)
    print()

    # Errors
    if stats["errors"]:
        print("Errors Encountered:")
        print("-" * 70)
        for error in stats["errors"]:
            print(f"  • {error}")
        print()
    else:
        print("✓ No errors encountered!")
        print()

    print("=" * 70)
    print("Reorganization Complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
