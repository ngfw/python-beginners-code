#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 21: Practical Example - Word Counter
"""

def count_words(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

text = "the quick brown fox jumps over the lazy dog the dog"
counts = count_words(text)
print(counts)
# {'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1,
#  'over': 1, 'lazy': 1, 'dog': 2}
