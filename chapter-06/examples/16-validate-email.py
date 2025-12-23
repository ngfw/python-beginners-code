#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 16: Validate Email Format (Simple)

Demonstrates a simple email validation function using string methods.
Note: This is a basic validation; real email validation is more complex.
"""

def is_valid_email(email):
    """Simple email validation"""
    if "@" not in email:
        return False
    if email.count("@") != 1:
        return False
    if "." not in email.split("@")[1]:
        return False
    return True

# Test the function
print(f"is_valid_email('alice@example.com'): {is_valid_email('alice@example.com')}")  # True
print(f"is_valid_email('invalid'): {is_valid_email('invalid')}")            # False
print(f"is_valid_email('no@domain'): {is_valid_email('no@domain')}")          # False
