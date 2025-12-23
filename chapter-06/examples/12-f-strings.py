#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 12: f-Strings (Recommended)

Demonstrates f-strings (formatted string literals) - Python 3.6+:
- Basic usage
- Expressions inside f-strings
- Formatting numbers
- Multi-line f-strings
- Debugging with f-strings (Python 3.8+)
"""

name = "Alice"
age = 25

# Basic usage
print(f"My name is {name} and I'm {age} years old")

# Expressions inside f-strings
print(f"Next year I'll be {age + 1}")

# Formatting numbers
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")  # 2 decimal places

price = 1234.56
print(f"Price: ${price:,.2f}")  # Price: $1,234.56 (with commas)

# Multiple lines
message = f"""
Hello, {name}!
You are {age} years old.
Next year you'll be {age + 1}.
"""
print(message)

# Debugging (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")  # x=10, y=20, x+y=30
