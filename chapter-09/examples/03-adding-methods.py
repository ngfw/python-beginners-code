#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 3: Adding Methods

Demonstrates adding methods (functions) to a class.
"""

class Dog:
    species = "Canis familiaris"

    def bark(self):
        print("Woof! Woof!")

    def sit(self):
        print("The dog is now sitting")

# Create instance and call methods
buddy = Dog()
print("Calling buddy.bark():")
buddy.bark()  # Woof! Woof!

print("\nCalling buddy.sit():")
buddy.sit()   # The dog is now sitting
