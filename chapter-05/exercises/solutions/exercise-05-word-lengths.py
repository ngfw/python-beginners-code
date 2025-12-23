#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Exercise 5.5: Write a program that takes a sentence and returns a dictionary with each word and its length.
"""

def word_lengths(sentence):
    words = sentence.split()
    return {word: len(word) for word in words}

sentence = "Python is an amazing programming language"
result = word_lengths(sentence)
print(result)
# {'Python': 6, 'is': 2, 'an': 2, 'amazing': 7, 'programming': 11, 'language': 8}
