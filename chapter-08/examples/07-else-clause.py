#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 7: The else Clause

Demonstrates the else clause that runs when no exception occurs.
"""

print("=== Using else Clause ===\n")

def divide_numbers(a_str, b_str):
    try:
        number = int(a_str)
        divisor = int(b_str)
        result = number / divisor
    except ValueError:
        print("Invalid number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        # Only runs if no exception occurred
        print(f"Result: {result}")
        print("Calculation successful!")

# Test cases
print("Test 1: Valid inputs (10, 2)")
divide_numbers("10", "2")

print("\nTest 2: Invalid input (abc, 5)")
divide_numbers("abc", "5")

print("\nTest 3: Division by zero (10, 0)")
divide_numbers("10", "0")
