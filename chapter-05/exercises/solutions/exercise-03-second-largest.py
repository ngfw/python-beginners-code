#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Exercise 5.3: Given a list of numbers, find the second largest number.
"""

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

numbers = [10, 5, 20, 8, 20, 15]
print("Numbers:", numbers)
print("Second largest:", second_largest(numbers))  # 15
