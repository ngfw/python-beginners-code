#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 3: Accessing List Elements
"""

fruits = ["apple", "banana", "cherry", "date"]

print("=== Basic indexing ===")
print(fruits[0])   # apple (first item)
print(fruits[1])   # banana
print(fruits[3])   # date (fourth item)

print("\n=== Negative indexing (count from the end) ===")
print(fruits[-1])  # date (last item)
print(fruits[-2])  # cherry (second to last)

print("\n=== Slicing (get a range) ===")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4] (index 2 to 4)
print(numbers[:3])     # [0, 1, 2] (start to index 2)
print(numbers[5:])     # [5, 6, 7, 8, 9] (index 5 to end)
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd item)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
