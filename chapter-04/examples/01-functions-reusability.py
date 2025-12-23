#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 1: Functions Reusability
"""

print("=== Without functions (repetitive) ===")
print("Hello, Alice!")
print("Hello, Bob!")
print("Hello, Charlie!")

print("\n=== With functions (efficient) ===")
def greet(name):
    print("Hello,", name + "!")

greet("Alice")
greet("Bob")
greet("Charlie")
