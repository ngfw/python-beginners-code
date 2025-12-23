#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 21: Print Debug Information

Demonstrates printing debug information for troubleshooting.
"""

def process_data(data):
    """Process data with debug information"""
    print(f"DEBUG: Received data: {data}")
    print(f"DEBUG: Data type: {type(data)}")

    try:
        result = data / 2
        print(f"DEBUG: Result: {result}")
        return result
    except Exception as e:
        print(f"DEBUG: Error occurred: {e}")
        print(f"DEBUG: Error type: {type(e).__name__}")
        raise

print("=== Debug Information Demo ===\n")

# Test with valid data
print("Test 1: Valid data (10)")
try:
    result = process_data(10)
    print(f"✓ Success: {result}\n")
except Exception:
    pass

# Test with invalid data
print("Test 2: Invalid data ('abc')")
try:
    result = process_data("abc")
    print(f"✓ Success: {result}\n")
except Exception as e:
    print(f"✗ Failed as expected: {e}\n")
