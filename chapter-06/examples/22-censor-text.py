#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 22: Censoring Words

Demonstrates replacing bad words with asterisks.
"""

def censor_text(text, bad_words):
    """Censor bad words by replacing them with asterisks"""
    words = text.split()
    censored = []
    for word in words:
        if word.lower() in bad_words:
            censored.append("*" * len(word))
        else:
            censored.append(word)
    return " ".join(censored)

text = "This is a bad word example"
bad_words = ["bad", "example"]
print(f"Original: {text}")
print(f"Censored: {censor_text(text, bad_words)}")  # This is a *** word *******
