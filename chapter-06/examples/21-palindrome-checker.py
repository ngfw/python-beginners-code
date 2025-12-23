#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 21: Check if Palindrome

Demonstrates checking if a string is a palindrome (reads the same forwards and backwards).
"""

def is_palindrome(text):
    """Check if text is a palindrome"""
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")      # True
print(f"is_palindrome('hello'): {is_palindrome('hello')}")        # False

# Complex example
phrase = "A man a plan a canal Panama"
cleaned_phrase = phrase.replace(" ", "").lower()
print(f"is_palindrome('{phrase}'): {is_palindrome(phrase)}")  # True
