#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Example 17: Simple Calculator Program
Putting it all together!
"""

print("=== Simple Calculator ===")
print()

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Display results
print()
print("Results:")
print("--------")
print("Addition:", num1, "+", num2, "=", addition)
print("Subtraction:", num1, "-", num2, "=", subtraction)
print("Multiplication:", num1, "×", num2, "=", multiplication)
print("Division:", num1, "÷", num2, "=", division)
