#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 12: Creating and Basic Set Operations
"""

print("=== Creating sets ===")
# Using curly braces
fruits = {"apple", "banana", "cherry"}
print("Fruits set:", fruits)

# From a list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 3])
print("Numbers set:", numbers)  # {1, 2, 3}

# Empty set (must use set(), not {})
empty_set = set()
print("Empty set:", empty_set)

print("\n=== Set operations ===")
fruits = {"apple", "banana", "cherry"}

# Add item
fruits.add("date")
print("After add:", fruits)

# Remove item
fruits.remove("banana")  # Error if item doesn't exist
print("After remove:", fruits)

# Check membership
print("'apple' in fruits:", "apple" in fruits)  # True

# Length
print("Length:", len(fruits))
