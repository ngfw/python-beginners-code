#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 4: Count Words in File

Demonstrates reading a file and counting words with error handling.
"""

def count_words_in_file(filename):
    """Count words in a file"""
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found"

# Create a sample file first
with open("example.txt", "w") as f:
    f.write("Python is awesome and powerful")

# Count words
count = count_words_in_file("example.txt")
print(f"Word count: {count}")

# Test with non-existent file
count = count_words_in_file("nonexistent.txt")
print(f"Non-existent file: {count}")
