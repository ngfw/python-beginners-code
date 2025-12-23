#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Exercise 6.8: Caesar Cipher

Create a simple text-based encryption using Caesar cipher
(shift each letter by n positions in the alphabet).
"""

def caesar_cipher(text, shift):
    """Encrypt text using Caesar cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Handle lowercase
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    """Decrypt text using Caesar cipher"""
    return caesar_cipher(text, -shift)

# Test the functions
original = "Hello, World!"
print(f"Original: {original}")

encrypted = caesar_cipher(original, 3)
print(f"Encrypted (shift 3): {encrypted}")  # Khoor, Zruog!

decrypted = caesar_decipher(encrypted, 3)
print(f"Decrypted: {decrypted}")  # Hello, World!
