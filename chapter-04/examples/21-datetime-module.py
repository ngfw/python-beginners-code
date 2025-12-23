#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 21: datetime Module Examples
"""

import datetime

print("=== Current date and time ===")
now = datetime.datetime.now()
print(now)

print("\n=== Current date ===")
today = datetime.date.today()
print(today)

print("\n=== Format date ===")
print(today.strftime("%B %d, %Y"))  # e.g., January 15, 2025

print("\n=== Create specific date ===")
birthday = datetime.date(1995, 5, 20)
print(birthday)
