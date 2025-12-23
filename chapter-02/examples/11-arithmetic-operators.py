#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Example 11: Arithmetic Operators
"""

print("=== Basic Arithmetic Operators ===")
# Addition
print("10 + 5 =", 10 + 5)  # 15

# Subtraction
print("10 - 5 =", 10 - 5)  # 5

# Multiplication
print("10 * 5 =", 10 * 5)  # 50

# Division (always returns float)
print("10 / 5 =", 10 / 5)  # 2.0
print("10 / 3 =", 10 / 3)  # 3.3333333333333335

# Floor Division (integer division)
print("10 // 3 =", 10 // 3)  # 3 (rounds down)

# Modulus (remainder)
print("10 % 3 =", 10 % 3)  # 1 (10 divided by 3 has remainder 1)

# Exponentiation (power)
print("2 ** 3 =", 2 ** 3)  # 8 (2 to the power of 3)
print("5 ** 2 =", 5 ** 2)  # 25 (5 squared)

print("\n=== Practical Examples ===")

# Calculate area of a rectangle
length = 10
width = 5
area = length * width
print("Area:", area)  # Area: 50

# Calculate average
num1 = 80
num2 = 90
num3 = 85
average = (num1 + num2 + num3) / 3
print("Average:", average)  # Average: 85.0

# Check if number is even (remainder is 0)
number = 42
remainder = number % 2
print("Remainder of 42 % 2:", remainder)  # 0 (means it's even)
