#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 6: List Comprehension
"""

print("=== Traditional way ===")
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print("\n=== List comprehension (one line!) ===")
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print("\n=== With condition ===")
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

print("\n=== More examples ===")
fruits = ["apple", "banana", "cherry"]
uppercase = [fruit.upper() for fruit in fruits]
print(uppercase)  # ["APPLE", "BANANA", "CHERRY"]
