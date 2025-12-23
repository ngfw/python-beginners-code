#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 7: Save User Data with Timestamp

Demonstrates saving notes with timestamps.
"""

import datetime

def save_notes(filename, note):
    """Save a note with timestamp"""
    with open(filename, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {note}\n")

# Use it
save_notes("notes.txt", "Learned about file I/O today!")
save_notes("notes.txt", "Python is awesome!")

print("Notes saved to notes.txt")

# Read to verify
with open("notes.txt", "r") as file:
    print("\n=== Notes: ===")
    print(file.read())
