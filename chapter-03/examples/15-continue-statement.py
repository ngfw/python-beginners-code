#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 15: continue Statement
"""

print("=== Skip even numbers ===")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip the print for even numbers
    print(i)
# Output: 1, 3, 5, 7, 9 (only odd numbers)

print("\n=== Practical example: Filter ===")
# Process only positive numbers
numbers = [10, -5, 20, -3, 15, -8, 25]

for num in numbers:
    if num < 0:
        continue  # Skip negative numbers
    print("Processing:", num)
    # Do something with positive numbers
