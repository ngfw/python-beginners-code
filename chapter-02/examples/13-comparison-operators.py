#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Example 13: Comparison Operators
"""

print("=== Comparison Operators ===")

# Equal to
print("5 == 5:", 5 == 5)  # True
print("5 == 3:", 5 == 3)  # False

# Not equal to
print("5 != 3:", 5 != 3)  # True
print("5 != 5:", 5 != 5)  # False

# Greater than
print("10 > 5:", 10 > 5)  # True
print("5 > 10:", 5 > 10)  # False

# Less than
print("5 < 10:", 5 < 10)  # True
print("10 < 5:", 10 < 5)  # False

# Greater than or equal to
print("10 >= 10:", 10 >= 10)  # True
print("10 >= 5:", 10 >= 5)  # True

# Less than or equal to
print("5 <= 10:", 5 <= 10)  # True
print("5 <= 5:", 5 <= 5)  # True

print("\n=== Practical Example ===")

age = 18
drinking_age = 21

can_drink = age >= drinking_age
print("Can drink:", can_drink)  # False
