#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 7: Count Occurrences

Demonstrates counting substrings in a string.
"""

text = "Hello, World! Hello, Python!"

print(f"Text: {text}")
print(f"Count 'Hello': {text.count('Hello')}")  # 2
print(f"Count 'l': {text.count('l')}")      # 3
print(f"Count 'Java': {text.count('Java')}")   # 0
