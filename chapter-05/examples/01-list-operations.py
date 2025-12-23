#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example: List Operations
"""

# Create list
fruits = ["apple", "banana", "cherry"]

# Add items
fruits.append("date")
print("After append:", fruits)

fruits.insert(1, "avocado")
print("After insert:", fruits)

# Remove items
fruits.remove("cherry")
print("After remove:", fruits)

last_item = fruits.pop()
print("Popped:", last_item)
print("After pop:", fruits)

# List comprehension
squares = [i ** 2 for i in range(10)]
print("Squares:", squares)

even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print("Even squares:", even_squares)
