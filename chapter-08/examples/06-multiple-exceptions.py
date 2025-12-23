#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 6: Handling Multiple Exceptions

Demonstrates two ways to handle multiple exception types.
"""

print("=== Method 1: Same handling for multiple exceptions ===\n")

def test_method1(value):
    try:
        number = int(value)
        result = 10 / number
        print(f"Result: {result}")
    except (ValueError, ZeroDivisionError):
        print("Invalid input or division by zero!")

test_method1("abc")
test_method1("0")

print("\n=== Method 2: Different handling for each ===\n")

def test_method2(items, index_str):
    try:
        numbers = items
        index = int(index_str)
        print(f"Value at index {index}: {numbers[index]}")
    except ValueError:
        print("Please enter a number!")
    except IndexError:
        print("Index out of range!")
    except Exception as e:
        print(f"Unexpected error: {e}")

numbers = [1, 2, 3]
test_method2(numbers, "1")   # Valid
test_method2(numbers, "abc") # ValueError
test_method2(numbers, "10")  # IndexError
