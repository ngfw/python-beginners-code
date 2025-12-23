#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 3: Reading Line by Line

Demonstrates three methods for reading files line by line:
1. readlines() - reads all lines into a list
2. Iterate directly (memory efficient)
3. readline() - read one line at a time
"""

# Create a sample file first
with open("example.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\nLine 4\n")

print("=== Method 1: readlines() ===")
# Read all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes newline characters

print("\n=== Method 2: Iterate directly (best) ===")
# Better: iterate directly (memory efficient)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\n=== Method 3: readline() ===")
# Read one line at a time
with open("example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"First line: {line1.strip()}")
    print(f"Second line: {line2.strip()}")
