#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 1: Basic File Reading

Demonstrates the basic way to open and read a file.
Note: Always remember to close files!
"""

# Create a sample file first
with open("example.txt", "w") as f:
    f.write("Hello from Python!\nThis is line 2.\nThis is line 3.")

# Basic file reading (not recommended - must close manually)
file = open("example.txt", "r")  # "r" = read mode
content = file.read()
print(content)
file.close()  # Always close files!

print("\n✓ File read and closed successfully")
