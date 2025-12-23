#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Exercise 5.4: Create a dictionary representing a book (title, author, year, pages). Print all key-value pairs.
"""

book = {
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "year": 2019,
    "pages": 544
}

for key, value in book.items():
    print(f"{key}: {value}")
