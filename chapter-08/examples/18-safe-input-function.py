#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 18: Safe Input Function

Demonstrates a robust input function with validation and error handling.
"""

def get_int_input(prompt, min_value=None, max_value=None):
    """Get integer input with validation
    
    In this demo version, we simulate user input instead of using input().
    """
    test_values = ["25", "abc", "-5", "200", "50"]
    
    print(f"\n=== Testing: {prompt} ===")
    for test_value in test_values:
        print(f"\nSimulated input: '{test_value}'")
        try:
            value = int(test_value)

            if min_value is not None and value < min_value:
                print(f"  ✗ Value must be at least {min_value}")
                continue

            if max_value is not None and value > max_value:
                print(f"  ✗ Value must be at most {max_value}")
                continue

            print(f"  ✓ Valid value: {value}")
            return value

        except ValueError:
            print("  ✗ Please enter a valid number!")
    
    return None

# Usage
result = get_int_input("Enter your age (0-150): ", 0, 150)
if result:
    print(f"\nFinal result: {result}")
