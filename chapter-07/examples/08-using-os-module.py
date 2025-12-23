#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 8: Using os Module

Demonstrates file and directory operations using the os module.
"""

import os

# Get current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Create a test file
with open("test_file.txt", "w") as f:
    f.write("Test content")

# Check if file exists
if os.path.exists("test_file.txt"):
    print("✓ test_file.txt exists!")

# Check if it's a file or directory
print(f"Is file: {os.path.isfile('test_file.txt')}")
print(f"Is directory: {os.path.isdir('test_file.txt')}")

# Get file size
size = os.path.getsize("test_file.txt")
print(f"File size: {size} bytes")

# List files in current directory (first 5)
files = os.listdir(".")
print(f"\nFiles in current directory (first 5): {files[:5]}")

# Join paths (cross-platform)
path = os.path.join("folder", "subfolder", "file.txt")
print(f"\nJoined path: {path}")

# Get filename and extension
filename = "document.pdf"
name, ext = os.path.splitext(filename)
print(f"\nFilename: {filename}")
print(f"Name: {name}, Extension: {ext}")
