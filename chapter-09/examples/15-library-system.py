#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 15: Simple Library System (Practical Project)

Demonstrates a complete library management system with Book and Library classes.
"""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} [{status}]"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def list_books(self):
        print(f"\n=== {self.name} Library ===")
        if not self.books:
            print("No books in library")
            return
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You borrowed: {book.title}")
                    return True
                else:
                    print(f"Sorry, {book.title} is already borrowed")
                    return False
        print("Book not found")
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Thank you for returning: {book.title}")
                    return True
                else:
                    print(f"{book.title} was not borrowed")
                    return False
        print("Book not found")
        return False

# Usage
print("=== Library System Demo ===\n")

library = Library("City Central")

book1 = Book("1984", "George Orwell", "001")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "002")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "003")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()

print("\nBorrowing book 001...")
library.borrow_book("001")

print("\nTrying to borrow book 001 again...")
library.borrow_book("001")  # Already borrowed

library.list_books()

print("\nReturning book 001...")
library.return_book("001")

library.list_books()
