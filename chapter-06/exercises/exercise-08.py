#!/usr/bin/env python3

"""
Chapter 6: Working with Strings
Exercise 6.8: Caesar Cipher

Create a simple text-based encryption using Caesar cipher
(shift each letter by n positions in the alphabet).


TODO: Complete the exercises below
"""

def caesar_cipher(text, shift):
    """Encrypt text using Caesar cipher"""
    # TODO: Your code here
    pass

def caesar_decipher(text, shift):
    """Decrypt text using Caesar cipher"""
    # TODO: Your code here
    pass

# Test the functions
original = "Hello, World!"

# Test cases
# TODO: Uncomment and complete
# print(f"Original: {original}")

encrypted = caesar_cipher(original, 3)

# Test cases
# TODO: Uncomment and complete
# print(f"Encrypted (shift 3): {encrypted}")  # Khoor, Zruog!

decrypted = caesar_decipher(encrypted, 3)

# Test cases
# TODO: Uncomment and complete
# print(f"Decrypted: {decrypted}")  # Hello, World!