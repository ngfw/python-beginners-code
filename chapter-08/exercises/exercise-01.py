#!/usr/bin/env python3

"""
Chapter 8: Error Handling
Exercise 8.1: Safe Integer Conversion

Write a function that safely converts a string to an integer,
returning a default value if conversion fails.


TODO: Complete the exercises below
"""

def safe_int(value, default=0):
    """Safely convert value to int, return default if it fails"""
    # TODO: Your code here
    pass

# Test the function

# Test cases
# TODO: Uncomment and complete
# print("=== safe_int() Tests ===\n")

test_cases = [
    ("123", 0, "Valid integer string"),
    ("abc", 0, "Invalid string"),
    ("45", -1, "Valid with custom default"),
    ("xyz", -1, "Invalid with custom default"),
    (42, 0, "Already an integer"),
    (None, 0, "None value"),
]

for value, default, description in test_cases:
    result = safe_int(value, default)

# Test cases
# TODO: Uncomment and complete
#     print(f"{description}: safe_int({repr(value)}, {default}) = {result}")