#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 11: Validating Input with Exceptions

Demonstrates comprehensive input validation using exceptions.
"""

def set_age(age):
    """Set age with validation"""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer!")
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age

print("=== Age Validation ===\n")

# Test cases
test_cases = [
    (25, "Valid age"),
    ("25", "String instead of int"),
    (-5, "Negative age"),
    (200, "Unrealistic age")
]

for test_age, description in test_cases:
    print(f"Test: {description} ({test_age})")
    try:
        result = set_age(test_age)
        print(f"  ✓ Age set to {result}")
    except (TypeError, ValueError) as e:
        print(f"  ✗ Invalid age: {e}")
    print()
