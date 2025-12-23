#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 16: Best Practice - Use Exceptions for Exceptional Cases

Demonstrates when to use exceptions vs. validation.
"""

print("=== Bad: Using Exceptions for Normal Flow ===\n")

def bad_example(age_input):
    try:
        user_age = int(age_input)
    except ValueError:
        user_age = 0  # Default value
    return user_age

print(f"Bad example with 'abc': {bad_example('abc')}")
print("✗ Using exceptions for expected cases is inefficient\n")

print("=== Good: Validate First ===\n")

def good_example(age_input):
    if age_input.isdigit():
        user_age = int(age_input)
    else:
        user_age = 0
    return user_age

print(f"Good example with 'abc': {good_example('abc')}")
print(f"Good example with '25': {good_example('25')}")
print("✓ Validation is clearer and more efficient")
