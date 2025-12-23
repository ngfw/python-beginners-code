#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 10: Raising Exceptions

Demonstrates how to raise your own exceptions.
"""

print("=== Basic raise ===\n")

def divide(a, b):
    """Divide two numbers with validation"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Test cases
print("Test 1: Valid division (10, 2)")
try:
    result = divide(10, 2)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")

print("\nTest 2: Division by zero (10, 0)")
try:
    result = divide(10, 0)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")
