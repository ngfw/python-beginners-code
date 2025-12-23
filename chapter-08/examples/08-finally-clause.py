#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 8: The finally Clause

Demonstrates the finally clause that always runs, regardless of exceptions.
"""

print("=== Using finally Clause ===\n")

def read_file_demo(filename):
    """Demonstrate finally clause with file handling"""
    file = None
    try:
        file = open(filename, "r")
        content = file.read()
        print(f"Content: {content}")
    except FileNotFoundError:
        print(f"File {filename} not found!")
    finally:
        # Always runs (cleanup code)
        if file:
            file.close()
            print("File closed")
        else:
            print("No file to close")

# Create a test file
with open("test.txt", "w") as f:
    f.write("Hello, World!")

print("Test 1: File exists")
read_file_demo("test.txt")

print("\nTest 2: File doesn't exist")
read_file_demo("nonexistent.txt")

print("\n=== Note: Using 'with' statement is better ===")
try:
    with open("test.txt", "r") as file:
        content = file.read()
        print(f"Content: {content}")
except FileNotFoundError:
    print("File not found!")
print("File automatically closed by 'with' statement")
