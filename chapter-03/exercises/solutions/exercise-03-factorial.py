#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Exercise 3.3: Write a program that calculates the factorial of a number (e.g., 5! = 5 × 4 × 3 × 2 × 1).
"""

number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial of", number, "is", factorial)
