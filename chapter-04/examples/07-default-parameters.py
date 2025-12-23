#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 7: Default Parameters
"""

def greet(name="Friend"):
    print("Hello,", name + "!")

greet("Alice")  # Hello, Alice!
greet()         # Hello, Friend! (uses default)

print("\n=== Multiple defaults ===")

def order_coffee(size="medium", milk=True, sugar=0):
    print(f"Order: {size} coffee")
    if milk:
        print("With milk")
    if sugar > 0:
        print(f"With {sugar} sugar(s)")

print("Default order:")
order_coffee()                      # Uses all defaults
print("\nLarge coffee:")
order_coffee("large")               # Large, with milk, no sugar
print("\nSmall, no milk, 2 sugars:")
order_coffee("small", False, 2)     # Small, no milk, 2 sugars
print("\nMedium with 3 sugars (keyword argument):")
order_coffee(sugar=3)               # Medium, milk, 3 sugars (keyword argument)
