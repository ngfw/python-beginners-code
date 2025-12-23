#!/usr/bin/env python3

"""
Chapter 6: Working with Strings
Exercise 6.4: Username Validator

Create a username validator that checks if a username is:
- 3-15 characters long
- Alphanumeric
- Starts with a letter


TODO: Complete the exercises below
"""

def is_valid_username(username):
    """Validate username according to rules"""
    # TODO: Your code here
    pass

# Test the function

# Test cases
# TODO: Uncomment and complete
# print(f"is_valid_username('Alice123'): {is_valid_username('Alice123')}")   # True
# print(f"is_valid_username('AB'): {is_valid_username('AB')}")         # False (too short)
# print(f"is_valid_username('123Alice'): {is_valid_username('123Alice')}")   # False (starts with number)
# print(f"is_valid_username('Alice@123'): {is_valid_username('Alice@123')}")  # False (contains @)