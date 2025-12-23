#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 17: Binary Files

Demonstrates working with binary files (images, videos, etc.).
"""

print("=== Creating a test binary file ===")
# Create a test binary file
test_data = b"Binary data content"
with open("test_binary.bin", "wb") as file:
    file.write(test_data)
print("✓ Created test_binary.bin")

print("\n=== Reading binary file ===")
# Read binary file
with open("test_binary.bin", "rb") as file:  # "rb" = read binary
    data = file.read()
    print(f"File size: {len(data)} bytes")
    print(f"Data: {data}")

print("\n=== Copying a file ===")
# Copy a file
with open("test_binary.bin", "rb") as source:
    with open("copy_binary.bin", "wb") as destination:  # "wb" = write binary
        destination.write(source.read())

print("✓ Copied to copy_binary.bin")

# Verify the copy
with open("copy_binary.bin", "rb") as file:
    copied_data = file.read()
    print(f"Copied file size: {len(copied_data)} bytes")
    print(f"Copy matches original: {copied_data == test_data}")
