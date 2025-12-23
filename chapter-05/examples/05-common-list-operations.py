#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 5: Common List Operations
"""

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Length
print("Length:", len(numbers))  # 8

# Check if item exists
print("3 in numbers:", 3 in numbers)  # True
print("10 in numbers:", 10 in numbers)  # False

# Count occurrences
print("Count of 1:", numbers.count(1))  # 2

# Find index
print("Index of 4:", numbers.index(4))  # 2 (first occurrence)

# Sort (modifies the list)
numbers.sort()
print("After sort:", numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse
numbers.reverse()
print("After reverse:", numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Copy a list
numbers_copy = numbers.copy()
print("Copy:", numbers_copy)

# Clear all items
numbers.clear()
print("After clear:", numbers)  # []
