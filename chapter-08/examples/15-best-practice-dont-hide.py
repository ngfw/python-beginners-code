#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 15: Best Practice - Don't Hide Errors

Demonstrates why you shouldn't silently hide errors.
"""

def risky_operation():
    """Simulate a risky operation"""
    raise ValueError("Something went wrong!")

print("=== Bad: Silently Hiding Errors ===\n")

def bad_example():
    try:
        risky_operation()
        print("This won't print")
    except:
        pass  # Errors are completely hidden!
    print("✗ Operation completed (but did it really?)")

bad_example()

print("\n=== Good: Log or Handle Appropriately ===\n")

def good_example():
    try:
        risky_operation()
        print("This won't print")
    except Exception as e:
        print(f"Warning: Operation failed - {e}")
        # Take appropriate action
    print("✓ Error was logged and handled")

good_example()
