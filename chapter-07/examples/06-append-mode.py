#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 6: Append Mode

Demonstrates appending to files without overwriting existing content.
"""

# Create initial file
with open("log.txt", "w") as file:
    file.write("Initial log entry\n")

# Append to file (creates if doesn't exist)
with open("log.txt", "a") as file:
    file.write("New log entry\n")

with open("log.txt", "a") as file:
    file.write("Another log entry\n")

print("Appended to log.txt")

# Read to verify
with open("log.txt", "r") as file:
    print("\n=== File contents: ===")
    print(file.read())
