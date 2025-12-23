#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 23: String Encoding and Decoding

Demonstrates encoding strings to bytes and decoding bytes to strings.
"""

# Encode string to bytes
text = "Hello, World!"
encoded = text.encode("utf-8")
print(f"Original: {text}")
print(f"Encoded: {encoded}")  # b'Hello, World!'
print(f"Type: {type(encoded)}")  # <class 'bytes'>

# Decode bytes to string
decoded = encoded.decode("utf-8")
print(f"\nDecoded: {decoded}")  # Hello, World!
print(f"Type: {type(decoded)}")  # <class 'str'>
