#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 17: Title Case for Names

Demonstrates formatting names with proper capitalization.
"""

def format_name(name):
    """Handle names like "john o'connor" or "mary-jane smith" """
    return name.title()

print(format_name("john o'connor"))   # John O'Connor
print(format_name("mary-jane smith")) # Mary-Jane Smith
