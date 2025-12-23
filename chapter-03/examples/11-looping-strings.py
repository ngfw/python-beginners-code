#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 11: Looping Through Strings
"""

print("=== Loop through each character ===")
name = "Python"

for letter in name:
    print(letter)
# Output:
# P
# y
# t
# h
# o
# n

print("\n=== Count vowels in a word ===")
word = "programming"
vowel_count = 0

for letter in word:
    if letter in "aeiou":
        vowel_count += 1

print("Vowels:", vowel_count)  # 3
