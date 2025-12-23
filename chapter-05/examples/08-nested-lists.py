#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 8: Nested Lists
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("First row:", matrix[0])     # [1, 2, 3]
print("Element at [1][2]:", matrix[1][2])  # 6

print("\n=== Loop through nested list ===")
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
