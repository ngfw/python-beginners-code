#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Exercise 3.6: Create a program that counts how many times a specific letter appears in a word.
"""

word = input("Enter a word: ")
letter = input("Enter a letter to count: ")
count = 0

for char in word:
    if char.lower() == letter.lower():
        count += 1

print("The letter", letter, "appears", count, "times")
