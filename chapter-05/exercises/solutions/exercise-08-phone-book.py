#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Exercise 5.8: Create a phone book using a dictionary. Add a function to search by name.
"""

phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

def search_phone_book(name):
    if name in phone_book:
        return phone_book[name]
    else:
        return "Not found"

print("=== Search existing contacts ===")
print("Alice:", search_phone_book("Alice"))  # 555-1234
print("David:", search_phone_book("David"))  # Not found

print("\n=== Add new contact ===")
phone_book["David"] = "555-3456"
print("David:", search_phone_book("David"))  # 555-3456

print("\n=== All contacts ===")
for name, number in phone_book.items():
    print(f"{name}: {number}")
