#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Exercise 6.6: Find Longest Word

Create a function that returns the longest word in a sentence.
"""

def longest_word(sentence):
    """Find the longest word in a sentence"""
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def longest_word_alt(sentence):
    """Alternative using max()"""
    words = sentence.split()
    return max(words, key=len)

# Test the functions
sentence = "Python is an amazing programming language"
print(f"Sentence: {sentence}")
print(f"Longest word (loop): {longest_word(sentence)}")  # programming
print(f"Longest word (max): {longest_word_alt(sentence)}")  # programming
