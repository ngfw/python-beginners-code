#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 22: Using Assertions

Demonstrates using assertions for development and debugging.
Note: Assertions can be disabled with Python's -O flag.
"""

def calculate_average(numbers):
    """Calculate average with assertions for validation"""
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"

    return sum(numbers) / len(numbers)

print("=== Using Assertions ===\n")

# Test with valid data
print("Test 1: Valid data [10, 20, 30]")
try:
    avg = calculate_average([10, 20, 30])
    print(f"  ✓ Average: {avg}")
except AssertionError as e:
    print(f"  ✗ Assertion failed: {e}")

# Test with empty list
print("\nTest 2: Empty list []")
try:
    avg = calculate_average([])
    print(f"  ✓ Average: {avg}")
except AssertionError as e:
    print(f"  ✗ Assertion failed: {e}")

# Test with invalid data
print("\nTest 3: Invalid data [10, 'abc', 30]")
try:
    avg = calculate_average([10, "abc", 30])
    print(f"  ✓ Average: {avg}")
except AssertionError as e:
    print(f"  ✗ Assertion failed: {e}")

print("\nNote: Assertions are for development/debugging, not production error handling")
