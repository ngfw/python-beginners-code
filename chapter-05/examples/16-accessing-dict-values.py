#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 16: Accessing Dictionary Values
"""

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Using key
print("Name:", student["name"])  # Alice

# Using get() (safer - returns None if key doesn't exist)
print("Age:", student.get("age"))  # 20
print("Email:", student.get("email"))  # None
print("Email with default:", student.get("email", "Not provided"))  # Not provided
