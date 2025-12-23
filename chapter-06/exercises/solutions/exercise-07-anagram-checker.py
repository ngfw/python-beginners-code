#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Exercise 6.7: Anagram Checker

Write a function that checks if two strings are anagrams
(contain the same letters in different order).
"""

def are_anagrams(str1, str2):
    """Check if two strings are anagrams"""
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Sort and compare
    return sorted(str1) == sorted(str2)

# Test the function
print(f"are_anagrams('listen', 'silent'): {are_anagrams('listen', 'silent')}")  # True
print(f"are_anagrams('hello', 'world'): {are_anagrams('hello', 'world')}")    # False
print(f"are_anagrams('The Morse Code', 'Here come dots'): {are_anagrams('The Morse Code', 'Here come dots')}")  # True
