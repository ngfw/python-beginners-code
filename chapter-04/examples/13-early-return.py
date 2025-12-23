#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 13: Early Return
"""

def check_age(age):
    if age < 0:
        return "Invalid age"
    if age < 18:
        return "Minor"
    if age < 65:
        return "Adult"
    return "Senior"

print(check_age(15))   # Minor
print(check_age(30))   # Adult
print(check_age(-5))   # Invalid age
