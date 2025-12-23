#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 2: Using with Statement (Recommended)

Demonstrates the recommended way to read files using the with statement.
The file is automatically closed when the block ends.
"""

# Create a sample file first
with open("example.txt", "w") as f:
    f.write("Hello from Python!\nThis is line 2.\nThis is line 3.")

# Read with 'with' statement (recommended)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here

print("\n✓ File automatically closed after with block")
