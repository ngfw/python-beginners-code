#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 3: Strings are Immutable

Demonstrates that strings cannot be changed after creation.
Shows the proper way to "modify" a string by creating a new one.
"""

word = "Python"
print(f"Original word: {word}")

# This would cause an error:
# word[0] = "J"  # TypeError: 'str' object does not support item assignment

# Instead, create a new string
word = "J" + word[1:]
print(f"Modified word: {word}")  # Jython
