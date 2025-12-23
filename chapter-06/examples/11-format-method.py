#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 11: str.format() Method

Demonstrates the .format() method for string formatting:
- Positional arguments
- Named arguments
- Indexed arguments
- Formatting numbers
"""

name = "Alice"
age = 25

# Positional arguments
print("Positional:", "My name is {} and I'm {} years old".format(name, age))

# Named arguments
print("Named:", "My name is {n} and I'm {a} years old".format(n=name, a=age))

# Indexed arguments
print("Indexed:", "I'm {1} years old and my name is {0}".format(name, age))

# Formatting numbers
pi = 3.14159
print("Formatted number:", "Pi is approximately {:.2f}".format(pi))  # Pi is approximately 3.14
