#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 9: Check String Content

Demonstrates string validation methods:
- isalpha(), isdigit(), isalnum()
- isupper(), islower(), isspace()
- Practical use: input validation
"""

# Check if string contains only...
print("=== String Content Checks ===")
print(f"'hello'.isalpha(): {'hello'.isalpha()}")      # True (only letters)
print(f"'hello123'.isalpha(): {'hello123'.isalpha()}")   # False

print(f"'12345'.isdigit(): {'12345'.isdigit()}")      # True (only digits)
print(f"'123.45'.isdigit(): {'123.45'.isdigit()}")     # False

print(f"'hello123'.isalnum(): {'hello123'.isalnum()}")   # True (letters or digits)
print(f"'hello 123'.isalnum(): {'hello 123'.isalnum()}")  # False (space not allowed)

print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")      # True
print(f"'hello'.islower(): {'hello'.islower()}")      # True

print(f"'   '.isspace(): {'   '.isspace()}")        # True (only whitespace)

# Practical use: Validate input
print("\n=== Practical Input Validation ===")
print("This would normally use input(), but for demo purposes:")
age_input = "25"
if age_input.isdigit():
    age = int(age_input)
    print(f"Your age is {age}")
else:
    print("Invalid age!")

# Test with invalid input
age_input = "twenty-five"
if age_input.isdigit():
    age = int(age_input)
    print(f"Your age is {age}")
else:
    print("Invalid age!")
