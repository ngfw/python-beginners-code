#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 9: Special Methods (Magic Methods)

Demonstrates special methods like __str__, __repr__, __len__, __eq__.
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # Called by str() and print()
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        # Called by repr() - for developers
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        # Called by len()
        return self.pages

    def __eq__(self, other):
        # Called by ==
        return self.title == other.title and self.author == other.author

# Usage
print("=== Special Methods Demo ===\n")

book1 = Book("1984", "George Orwell", 328)
book2 = Book("1984", "George Orwell", 328)

print(f"str(book1): {book1}")  # '1984' by George Orwell (uses __str__)
print(f"repr(book1): {repr(book1)}")  # Book('1984', 'George Orwell', 328) (uses __repr__)
print(f"len(book1): {len(book1)}")  # 328 (uses __len__)
print(f"book1 == book2: {book1 == book2}")  # True (uses __eq__)
