#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 17: Modifying Dictionaries
"""

student = {"name": "Alice", "age": 20}
print("Original:", student)

# Add new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Modify existing value
student["age"] = 21
print("After modifying age:", student)

# Remove items
del student["grade"]
print("After deleting grade:", student)

student["age"] = 20  # Add it back for pop example
removed_value = student.pop("age")  # Returns the value
print("Popped value:", removed_value)
print("After popping age:", student)
