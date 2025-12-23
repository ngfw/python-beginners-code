#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 19: Looping Through Dictionaries
"""

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print("=== Loop through keys ===")
for key in student:
    print(key)

print("\n=== Loop through keys explicitly ===")
for key in student.keys():
    print(key)

print("\n=== Loop through values ===")
for value in student.values():
    print(value)

print("\n=== Loop through key-value pairs ===")
for key, value in student.items():
    print(f"{key}: {value}")
