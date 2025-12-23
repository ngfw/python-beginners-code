#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 24: Raw Strings

Demonstrates raw strings (r prefix) where backslashes are treated literally.
Useful for regex patterns and file paths.
"""

# Normal string (escape sequences processed)
path = "C:\\Users\\Alice\\Documents"
print(f"Normal string: {path}")  # C:\Users\Alice\Documents

# Raw string (backslashes treated literally)
path = r"C:\Users\Alice\Documents"
print(f"Raw string: {path}")  # C:\Users\Alice\Documents

# Useful for regular expressions
pattern = r"\d{3}-\d{3}-\d{4}"  # Phone number pattern
print(f"Regex pattern: {pattern}")
