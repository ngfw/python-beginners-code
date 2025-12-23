#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 6: Find and Replace

Demonstrates finding and replacing substrings:
- find(), startswith(), endswith()
- replace() with and without limits
"""

text = "Python is awesome. Python is powerful."

# Find substring
print("=== Finding Substrings ===")
print(f"Text: {text}")
print(f"text.find('Python'): {text.find('Python')}")      # 0 (first occurrence)
print(f"text.find('awesome'): {text.find('awesome')}")     # 10
print(f"text.find('Java'): {text.find('Java')}")        # -1 (not found)

# Check if starts/ends with
print("\n=== Starts/Ends With ===")
print(f"text.startswith('Python'): {text.startswith('Python')}")  # True
print(f"text.endswith('powerful.'): {text.endswith('powerful.')}")  # True

# Replace
print("\n=== Replace ===")
new_text = text.replace("Python", "JavaScript")
print(f"Replace all 'Python': {new_text}")

# Replace with limit
new_text = text.replace("Python", "Java", 1)  # Replace first occurrence only
print(f"Replace first 'Python': {new_text}")
