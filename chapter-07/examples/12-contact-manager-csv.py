#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 12: Contact Manager (CSV Practical)

Demonstrates a practical contact manager using CSV files.
"""

import csv

def save_contact(name, phone, email):
    """Save a contact to CSV file"""
    with open("contacts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

def load_contacts():
    """Load all contacts from CSV file"""
    contacts = []
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts

# Save contacts
print("=== Saving contacts ===")
save_contact("Alice", "555-1234", "alice@example.com")
save_contact("Bob", "555-5678", "bob@example.com")
print("✓ Contacts saved")

# Load and display
print("\n=== Loading contacts ===")
contacts = load_contacts()
for name, phone, email in contacts:
    print(f"{name}: {phone} ({email})")
