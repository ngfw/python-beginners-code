#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 5: Strip Whitespace

Demonstrates removing whitespace from strings:
- strip(), lstrip(), rstrip()
- Removing specific characters
- Practical use: cleaning user input
"""

text = "   Hello, World!   "

print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")   # "Hello, World!" (both ends)
print(f"lstrip(): '{text.lstrip()}'")  # "Hello, World!   " (left only)
print(f"rstrip(): '{text.rstrip()}'")  # "   Hello, World!" (right only)

# Remove specific characters
text2 = "***Hello***"
print(f"\nOriginal: '{text2}'")
print(f"strip('*'): '{text2.strip('*')}'")  # Hello

# Practical use: Clean user input
print("\n=== Cleaning User Input ===")
print("This would normally use input(), but for demo purposes:")
user_input = "  Alice  "
cleaned = user_input.strip()
print(f"Original: '{user_input}'")
print(f"Cleaned: '{cleaned}'")
