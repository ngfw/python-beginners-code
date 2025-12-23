#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 20: Reverse a String

Demonstrates two methods for reversing a string:
- Using slicing [::-1]
- Using reversed() function
"""

def reverse_string(text):
    """Reverse a string using slicing"""
    return text[::-1]

def reverse_string_alt(text):
    """Reverse a string using reversed()"""
    return "".join(reversed(text))

text = "Python"
print(f"Original: {text}")
print(f"Reversed (slicing): {reverse_string(text)}")  # nohtyP
print(f"Reversed (reversed()): {reverse_string_alt(text)}")  # nohtyP
