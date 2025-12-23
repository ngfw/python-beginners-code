#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Example 2: Variable Naming Rules and Conventions
"""

# Good variable names
user_name = "Bob"
total_price = 99.99
is_valid = True
student_count = 25

print("Good variable names:")
print("user_name:", user_name)
print("total_price:", total_price)
print("is_valid:", is_valid)
print("student_count:", student_count)

# Bad variable names (but technically valid)
x = "Bob"  # Not descriptive
usrNm = "Bob"  # Hard to read
n = 25  # What does n mean?

print("\nBad variable names (but they work):")
print("x:", x)
print("usrNm:", usrNm)
print("n:", n)

# Invalid variable names (commented out to avoid errors)
# 2fast = 100  # Can't start with number
# user-name = "Bob"  # Can't use hyphens
# for = 5  # Can't use keywords
