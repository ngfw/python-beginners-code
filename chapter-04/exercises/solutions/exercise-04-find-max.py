#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Exercise 4.4: Create a function find_max(numbers) that takes a list of numbers and returns the largest one.
(don't use the built-in max() function)
"""

def find_max(numbers):
    if len(numbers) == 0:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

print(find_max([3, 7, 2, 9, 4]))  # 9
