#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 18: Dictionary Methods
"""

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Get all keys
print("Keys:", student.keys())

# Get all values
print("Values:", student.values())

# Get all key-value pairs
print("Items:", student.items())

# Check if key exists
print("'name' in student:", "name" in student)  # True
print("'email' in student:", "email" in student)  # False

# Number of items
print("Length:", len(student))  # 3

# Clear all items
student_copy = student.copy()
student_copy.clear()
print("After clear:", student_copy)  # {}
