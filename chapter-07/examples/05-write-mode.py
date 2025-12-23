#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 5: Write Mode

Demonstrates writing to files in write mode.
WARNING: Write mode overwrites existing content!
"""

# Write to file (creates if doesn't exist, overwrites if exists)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

print("Written to output.txt")

# Write multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

print("Overwritten output.txt with multiple lines")

# Read to verify
with open("output.txt", "r") as file:
    print("\n=== File contents: ===")
    print(file.read())
