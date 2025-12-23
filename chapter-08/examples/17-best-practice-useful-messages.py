#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 17: Best Practice - Provide Useful Error Messages

Demonstrates the importance of clear error messages.
"""

print("=== Bad: Vague Error Message ===\n")

def bad_example(age):
    if age < 0 or age > 150:
        raise ValueError("Error!")  # Not helpful!

try:
    bad_example(-5)
except ValueError as e:
    print(f"✗ {e}")

print("\n=== Good: Clear Error Message ===\n")

def good_example(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")
    if age > 150:
        raise ValueError(f"Age must be between 0 and 150, got {age}")

try:
    good_example(-5)
except ValueError as e:
    print(f"✓ {e}")

try:
    good_example(200)
except ValueError as e:
    print(f"✓ {e}")
