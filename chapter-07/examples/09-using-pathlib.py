#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 9: Using pathlib Module (Modern Approach)

Demonstrates the modern pathlib module for file operations.
"""

from pathlib import Path

# Create a test file
test_path = Path("example.txt")
test_path.write_text("Hello, World!")

# Check if exists
if test_path.exists():
    print("✓ File exists!")

# Read file
content = test_path.read_text()
print(f"Content: {content}")

# Get file info
print(f"\nFile name: {test_path.name}")       # example.txt
print(f"Stem: {test_path.stem}")       # example
print(f"Suffix: {test_path.suffix}")     # .txt
print(f"Parent: {test_path.parent}")     # Current directory

# Join paths (using / operator)
path = Path("folder") / "subfolder" / "file.txt"
print(f"\nJoined path: {path}")

# Create directory
new_dir = Path("my_test_directory")
new_dir.mkdir(exist_ok=True)  # exist_ok=True prevents error if exists
print(f"✓ Created directory: {new_dir}")

# List files in current directory
print("\n=== Files in current directory: ===")
for i, file in enumerate(Path(".").iterdir()):
    print(f"  {file}")
    if i >= 4:  # Show only first 5
        print("  ...")
        break

# Find all Python files
print("\n=== Python files: ===")
for file in list(Path(".").glob("*.py"))[:3]:
    print(f"  {file}")
