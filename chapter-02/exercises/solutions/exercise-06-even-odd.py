#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Exercise 2.6: Check if a number is even or odd using the modulus operator.
"""

number = int(input("Enter a number: "))
remainder = number % 2

print("Remainder when divided by 2:", remainder)
# If remainder is 0, it's even; if 1, it's odd
