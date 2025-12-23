#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 14: Practical Use - Remove Duplicates
"""

numbers = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", numbers)

unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)  # [1, 2, 3, 4, 5] (order may vary)
