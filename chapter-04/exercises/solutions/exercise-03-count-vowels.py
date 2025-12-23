#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Exercise 4.3: Write a function count_vowels(text) that counts and returns the number of vowels in a string.
"""

def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in 'aeiou':
            count += 1
    return count

print(count_vowels("Hello World"))  # 3
print(count_vowels("Python"))       # 1
