#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 14: Multi-line Strings

Demonstrates different ways to create multi-line strings:
- Triple quotes (preserves formatting)
- Backslash continuation
- Parentheses for implicit line joining
"""

# Triple quotes preserve formatting
text = """
This is a multi-line string.
It preserves line breaks.
And indentation.
"""
print("Triple quotes:")
print(text)

# Use backslash to continue lines
long_text = "This is a very long line that " \
            "spans multiple lines in the code " \
            "but appears as one line when printed"
print("Backslash continuation:")
print(long_text)

# Parentheses for implicit line joining
message = ("This is also a long line "
           "that spans multiple lines "
           "in the code")
print("\nParentheses joining:")
print(message)
