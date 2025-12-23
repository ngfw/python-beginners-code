#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Exercise 6.3: Capitalize Sentences

Write a function that capitalizes the first letter of each sentence in a paragraph.
"""

def capitalize_sentences(text):
    """Capitalize the first letter of each sentence"""
    sentences = text.split(". ")
    capitalized = [s.capitalize() for s in sentences]
    return ". ".join(capitalized)

# Test the function
text = "hello world. python is awesome. let's learn!"
print(f"Original: {text}")
print(f"Capitalized: {capitalize_sentences(text)}")
# Hello world. Python is awesome. Let's learn!
