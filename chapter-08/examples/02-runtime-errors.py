#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 2: Runtime Errors (Exceptions)

Demonstrates common runtime errors.
Note: These are wrapped in try-except to show the errors without crashing.
"""

print("=== Runtime Error Examples ===\n")

# ZeroDivisionError
print("1. ZeroDivisionError:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   Error: {e}")

# NameError (variable doesn't exist)
print("\n2. NameError:")
try:
    print(unknown_variable)
except NameError as e:
    print(f"   Error: {e}")

# TypeError (wrong type)
print("\n3. TypeError:")
try:
    result = "5" + 5
except TypeError as e:
    print(f"   Error: {e}")

# IndexError (index out of range)
print("\n4. IndexError:")
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print(f"   Error: {e}")

# KeyError (dictionary key doesn't exist)
print("\n5. KeyError:")
try:
    person = {"name": "Alice"}
    print(person["age"])
except KeyError as e:
    print(f"   Error: {e}")

# ValueError (invalid value)
print("\n6. ValueError:")
try:
    number = int("abc")
except ValueError as e:
    print(f"   Error: {e}")

# FileNotFoundError
print("\n7. FileNotFoundError:")
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"   Error: {e}")
