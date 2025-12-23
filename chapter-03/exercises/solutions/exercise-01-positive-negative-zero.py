#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Exercise 3.1: Write a program that asks for a number and prints whether it's positive, negative, or zero.
"""

number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
