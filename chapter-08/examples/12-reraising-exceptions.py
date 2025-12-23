#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 12: Re-raising Exceptions

Demonstrates re-raising exceptions to handle them at multiple levels.
"""

def process_file(filename):
    """Process file with error logging and re-raising"""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        raise  # Re-raise the exception

print("=== Re-raising Exceptions ===\n")

# Test with non-existent file
try:
    content = process_file("missing.txt")
    print(f"Content: {content}")
except FileNotFoundError:
    print("Handling at higher level")
    print("✓ Exception was caught and re-raised successfully")

print("\n=== Test with existing file ===")
# Create a test file
with open("test.txt", "w") as f:
    f.write("Test content")

try:
    content = process_file("test.txt")
    print(f"Content: {content}")
    print("✓ File processed successfully")
except FileNotFoundError:
    print("This won't be reached")
