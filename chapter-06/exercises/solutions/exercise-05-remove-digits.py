#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Exercise 6.5: Remove Digits

Write a function that removes all digits from a string.
"""

def remove_digits(text):
    """Remove all digits from text"""
    return "".join([char for char in text if not char.isdigit()])

def remove_digits_alt(text):
    """Alternative implementation using loop"""
    result = ""
    for char in text:
        if not char.isdigit():
            result += char
    return result

# Test the functions
text = "Hello123World456"
print(f"Original: {text}")
print(f"Removed digits (comprehension): {remove_digits(text)}")  # HelloWorld
print(f"Removed digits (loop): {remove_digits_alt(text)}")  # HelloWorld
