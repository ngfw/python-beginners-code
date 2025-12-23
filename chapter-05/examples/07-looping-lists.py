#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 7: Looping Through Lists
"""

fruits = ["apple", "banana", "cherry"]

print("=== Simple loop ===")
for fruit in fruits:
    print(fruit)

print("\n=== Loop with index using range ===")
for i in range(len(fruits)):
    print(i, fruits[i])

print("\n=== Loop with enumerate (better!) ===")
for index, fruit in enumerate(fruits):
    print(index, fruit)
