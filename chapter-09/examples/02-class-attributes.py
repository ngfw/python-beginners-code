#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 2: Adding Class Attributes

Demonstrates class attributes that are shared by all instances.
"""

class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

# Create instances
buddy = Dog()
miles = Dog()

# Access class attribute
print(f"Buddy's species: {buddy.species}")  # Canis familiaris
print(f"Miles' species: {miles.species}")  # Canis familiaris

# All instances share the same class attribute
print(f"Same species: {buddy.species == miles.species}")  # True
