#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Exercise 4.1: Write a function is_even(number) that returns True if a number is even, False otherwise.
"""

def is_even(number):
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False
