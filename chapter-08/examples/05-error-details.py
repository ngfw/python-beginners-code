#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 5: Getting Error Details

Demonstrates how to capture and display error details.
"""

print("=== Getting Error Details ===\n")

def test_operation(value):
    """Test operation with error details"""
    try:
        number = int(value)
        result = 10 / number
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Error type: {type(e).__name__}")

# Test cases
print("Test 1: Invalid number")
test_operation("abc")

print("\nTest 2: Division by zero")
test_operation("0")

print("\nTest 3: Valid input")
test_operation("2")
