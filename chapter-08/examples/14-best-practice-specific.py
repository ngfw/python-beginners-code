#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 14: Best Practice - Be Specific

Demonstrates the importance of catching specific exceptions.
"""

print("=== Bad: Catching Everything ===\n")

def bad_example(value):
    """Bad practice: catches all exceptions"""
    try:
        result = int(value) / 0
    except:
        print("Error!")  # Don't know what went wrong!

bad_example("5")

print("\n=== Good: Specific Exceptions ===\n")

def good_example(value):
    """Good practice: specific exception handling"""
    try:
        result = int(value) / 0
    except ValueError:
        print("Invalid number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

good_example("5")

print("\n✓ Specific exceptions provide better error messages")
