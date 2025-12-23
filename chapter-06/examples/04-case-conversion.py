#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 4: Case Conversion Methods

Demonstrates string case conversion methods:
- upper(), lower(), capitalize(), title(), swapcase()
- Practical use: case-insensitive comparison
"""

text = "Hello, World!"

print(f"Original: {text}")
print(f"upper(): {text.upper()}")      # HELLO, WORLD!
print(f"lower(): {text.lower()}")      # hello, world!
print(f"capitalize(): {text.capitalize()}") # Hello, world!
print(f"title(): {text.title()}")      # Hello, World!
print(f"swapcase(): {text.swapcase()}") # hELLO, wORLD!

# Practical use: Case-insensitive comparison
print("\n=== Case-Insensitive Comparison ===")
password = "Python123"
user_input = "PYTHON123"
if password.lower() == user_input.lower():
    print("Match!")
