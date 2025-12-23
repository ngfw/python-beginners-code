#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 8: Keyword Arguments
"""

def introduce(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments
print("Positional arguments:")
introduce("Alice", 25, "Boston")

# Keyword arguments (order doesn't matter)
print("\nKeyword arguments:")
introduce(city="Boston", name="Alice", age=25)

# Mix (positional first, then keyword)
print("\nMixed arguments:")
introduce("Alice", city="Boston", age=25)
