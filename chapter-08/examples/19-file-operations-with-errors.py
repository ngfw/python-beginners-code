#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 19: File Operations with Error Handling

Demonstrates comprehensive error handling for file operations.
"""

def read_file_safely(filename):
    """Read file with comprehensive error handling"""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    except Exception as e:
        print(f"Unexpected error reading '{filename}': {e}")
        return None

def write_file_safely(filename, content):
    """Write file with error handling"""
    try:
        with open(filename, "w") as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"Error: No permission to write to '{filename}'")
        return False
    except Exception as e:
        print(f"Unexpected error writing to '{filename}': {e}")
        return False

# Test reading
print("=== Testing File Reading ===\n")

# Create a test file
with open("test_data.txt", "w") as f:
    f.write("Test content")

content = read_file_safely("test_data.txt")
if content:
    print(f"✓ File read successfully: {content}")

content = read_file_safely("nonexistent.txt")
if not content:
    print("✗ File read failed as expected")

# Test writing
print("\n=== Testing File Writing ===\n")

if write_file_safely("output.txt", "Hello, World!"):
    print("✓ File written successfully")

# Verify
content = read_file_safely("output.txt")
if content:
    print(f"✓ Verified content: {content}")
