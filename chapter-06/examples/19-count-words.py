#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 19: Count Words in Text

Demonstrates counting words in a text string.
"""

def count_words(text):
    """Count words in text"""
    words = text.split()
    return len(words)

text = "Python is a powerful programming language"
print(f"Word count: {count_words(text)}")  # Word count: 6
