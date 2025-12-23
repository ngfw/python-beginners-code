#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Exercise 6.1: Count Vowels and Consonants

Write a function that counts vowels and consonants in a string.
"""

def count_vowels_consonants(text):
    """Count vowels and consonants in text"""
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Test the function
text = "Hello, World!"
v, c = count_vowels_consonants(text)
print(f"Text: {text}")
print(f"Vowels: {v}, Consonants: {c}")  # Vowels: 3, Consonants: 7
