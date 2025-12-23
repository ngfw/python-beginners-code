#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 4: Catching Specific Exceptions

Demonstrates catching specific exception types for better error handling.
"""

print("=== Catching Specific Exceptions ===\n")

def test_input(user_input):
    """Test input with specific exception handling"""
    try:
        number = int(user_input)
        result = 10 / number
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter a valid number!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# Test cases
print("Test 1: Valid input (5)")
test_input("5")

print("\nTest 2: Invalid input (abc)")
test_input("abc")

print("\nTest 3: Zero input")
test_input("0")
