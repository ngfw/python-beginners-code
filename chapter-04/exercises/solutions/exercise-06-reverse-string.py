#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Exercise 4.6: Create a function reverse_string(text) that returns the reversed version of a string.
"""

def reverse_string(text):
    return text[::-1]

# Alternative without slicing:
def reverse_string_alt(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

print(reverse_string("Python"))      # nohtyP
print(reverse_string_alt("Python"))  # nohtyP
