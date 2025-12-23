#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Exercise 5.2: Write a function that takes a list of numbers and returns a new list with only the even numbers.
"""

def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Alternative
def get_even_numbers_alt(numbers):
    even_nums = []
    for num in numbers:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original:", numbers)
print("Even numbers (comprehension):", get_even_numbers(numbers))
print("Even numbers (loop):", get_even_numbers_alt(numbers))
