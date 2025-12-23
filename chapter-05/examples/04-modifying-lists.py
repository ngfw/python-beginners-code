#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 4: Modifying Lists
"""

fruits = ["apple", "banana", "cherry"]
print("Original:", fruits)

# Change an item
fruits[1] = "blueberry"
print("After change:", fruits)

# Add items
fruits.append("date")  # Add to end
print("After append:", fruits)

fruits.insert(1, "avocado")  # Insert at index 1
print("After insert:", fruits)

# Remove items
fruits.remove("cherry")  # Remove by value
print("After remove:", fruits)

last_item = fruits.pop()  # Remove and return last item
print("Popped item:", last_item)
print("After pop:", fruits)

del fruits[0]  # Delete by index
print("After del:", fruits)
