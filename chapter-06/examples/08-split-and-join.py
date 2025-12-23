#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 8: Split and Join

Demonstrates splitting strings into lists and joining lists into strings:
- split() - string to list
- join() - list to string
- Practical examples
"""

# Split (string → list)
print("=== Split (string → list) ===")
sentence = "Python is awesome"
words = sentence.split()  # Split by whitespace
print(f"Sentence: {sentence}")
print(f"Words: {words}")  # ['Python', 'is', 'awesome']

csv = "Alice,25,New York"
data = csv.split(",")  # Split by comma
print(f"\nCSV: {csv}")
print(f"Data: {data}")  # ['Alice', '25', 'New York']

# Join (list → string)
print("\n=== Join (list → string) ===")
words = ['Python', 'is', 'awesome']
sentence = " ".join(words)
print(f"Words: {words}")
print(f"Sentence: {sentence}")  # Python is awesome

# Join with different separator
csv = ",".join(['Alice', '25', 'New York'])
print(f"\nJoin with comma: {csv}")  # Alice,25,New York

# Practical example
print("\n=== Practical Path Example ===")
path_parts = ['home', 'user', 'documents']
path = "/".join(path_parts)
print(f"Path parts: {path_parts}")
print(f"Path: {path}")  # home/user/documents
