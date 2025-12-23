#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 16: Error Handling with Files

Demonstrates proper error handling when working with files.
"""

print("=== Handling FileNotFoundError ===")
# Handle file not found
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")

print("\n=== Handling PermissionError ===")
# Handle permission errors (simulated)
try:
    # This would fail with real protected file: /root/protected.txt
    with open("test_file.txt", "w") as file:
        file.write("test")
    print("✓ File written successfully")
except PermissionError:
    print("Error: Permission denied!")

print("\n=== General Exception Handling ===")
# General exception handling
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: Permission denied!")
except Exception as e:
    print(f"Error: {e}")
