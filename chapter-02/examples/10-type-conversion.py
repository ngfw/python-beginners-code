#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Example 10: Converting Between Types (Type Casting)
"""

# String to integer
age_text = "25"
age_number = int(age_text)
print("String '25' converted to int:", age_number + 5)  # 30

# Integer to string
score = 100
score_text = str(score)
print("Your score is: " + score_text)

# String to float
price_text = "19.99"
price = float(price_text)
print("String '19.99' converted to float:", price * 2)  # 39.98

# Integer to float
x = 5
y = float(x)
print("Integer 5 converted to float:", y)  # 5.0

# Float to integer (removes decimal part)
pi = 3.14159
pi_int = int(pi)
print("Float 3.14159 converted to int:", pi_int)  # 3

# Warning: Converting to int() truncates (doesn't round)
print("\nWarning - int() truncates, doesn't round:")
print("int(7.9) =", int(7.9))  # 7 (not 8!)
