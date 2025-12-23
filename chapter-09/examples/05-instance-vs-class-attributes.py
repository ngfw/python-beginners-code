#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 5: Instance Attributes vs Class Attributes

Demonstrates the difference between instance and class attributes.
"""

class Dog:
    # Class attribute (shared)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

buddy = Dog("Buddy", 3)
miles = Dog("Miles", 5)

# Instance attributes are different
print("=== Instance Attributes ===")
print(f"Buddy's name: {buddy.name}")  # Buddy
print(f"Miles' name: {miles.name}")  # Miles

# Class attribute is the same
print("\n=== Class Attribute ===")
print(f"Buddy's species: {buddy.species}")  # Canis familiaris
print(f"Miles' species: {miles.species}")  # Canis familiaris

# Modifying class attribute affects all instances
print("\n=== Modifying Class Attribute ===")
Dog.species = "Dog"
print(f"Buddy's species: {buddy.species}")  # Dog
print(f"Miles' species: {miles.species}")  # Dog
