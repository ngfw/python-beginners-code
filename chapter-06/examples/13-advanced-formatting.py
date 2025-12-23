#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 13: Advanced String Formatting

Demonstrates advanced formatting options:
- Padding and alignment
- Number formatting
- Binary, octal, hexadecimal
- Percentage formatting
"""

# Padding and alignment
text = "Python"
print(f"Right-aligned: '{text:>10}'")   # "    Python"
print(f"Left-aligned: '{text:<10}'")   # "Python    "
print(f"Centered: '{text:^10}'")   # "  Python  "
print(f"Centered with *: '{text:*^10}'")  # "**Python**"

# Number formatting
number = 42
print(f"\nZero-padded: {number:05d}")  # 00042 (zero-padded to 5 digits)

# Binary, octal, hex
number = 255
print(f"\nBinary: {number:b}")  # 11111111
print(f"Octal: {number:o}")  # 377
print(f"Hex (lowercase): {number:x}")  # ff
print(f"Hex (uppercase): {number:X}")  # FF

# Percentage
ratio = 0.85
print(f"\nPercentage: {ratio:.2%}")  # 85.00%
