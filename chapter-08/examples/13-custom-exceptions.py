#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 13: Custom Exception Classes

Demonstrates creating and using custom exception classes.
"""

class InvalidEmailError(Exception):
    """Raised when email format is invalid"""
    pass

class InvalidPasswordError(Exception):
    """Raised when password is too weak"""
    pass

def validate_email(email):
    """Validate email format"""
    if "@" not in email:
        raise InvalidEmailError(f"Invalid email: {email}")
    return True

def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters")
    return True

print("=== Custom Exceptions Demo ===\n")

# Test email validation
print("Test 1: Valid email")
try:
    validate_email("user@example.com")
    print("  ✓ Valid email")
except InvalidEmailError as e:
    print(f"  ✗ Email error: {e}")

print("\nTest 2: Invalid email")
try:
    validate_email("invalidemail")
    print("  ✓ Valid email")
except InvalidEmailError as e:
    print(f"  ✗ Email error: {e}")

# Test password validation
print("\nTest 3: Valid password")
try:
    validate_password("SecurePass123")
    print("  ✓ Valid password")
except InvalidPasswordError as e:
    print(f"  ✗ Password error: {e}")

print("\nTest 4: Invalid password")
try:
    validate_password("short")
    print("  ✓ Valid password")
except InvalidPasswordError as e:
    print(f"  ✗ Password error: {e}")
