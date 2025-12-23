#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Example 16: Getting User Input
"""

name = input("What is your name? ")
print("Hello,", name)

print("\n=== Converting Input to Numbers ===")

# input() always returns a string - must convert for math
age_str = input("How old are you? ")
age = int(age_str)  # Convert to integer
next_year = age + 1
print("Next year you'll be", next_year)

# Shortcut: Convert immediately
print("\n=== Shortcut Method ===")
favorite_number = int(input("What's your favorite number? "))
print("Your favorite number times 2 is:", favorite_number * 2)
