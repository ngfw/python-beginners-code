#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 20: Nested Dictionaries
"""

students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grade": "A"
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "grade": "B"
    }
}

print("Alice's name:", students["student1"]["name"])

print("\n=== Loop through nested dictionary ===")
for student_id, info in students.items():
    print(f"{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
