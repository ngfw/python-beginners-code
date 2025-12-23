#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Exercise 5.7: Write a function that removes duplicate items from a list while preserving order.
"""

def remove_duplicates(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

# Alternative using dict (preserves order in Python 3.7+)
def remove_duplicates_alt(items):
    return list(dict.fromkeys(items))

numbers = [1, 2, 2, 3, 4, 3, 5]
print("Original:", numbers)
print("Without duplicates (loop):", remove_duplicates(numbers))
print("Without duplicates (dict):", remove_duplicates_alt(numbers))
