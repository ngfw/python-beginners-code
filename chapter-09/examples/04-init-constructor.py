#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 4: The __init__ Constructor

Demonstrates using __init__ to initialize objects with instance attributes.
"""

class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create instances with different attributes
buddy = Dog("Buddy", 3)
miles = Dog("Miles", 5)

print(buddy.description())  # Buddy is 3 years old
print(miles.description())  # Miles is 5 years old

print(buddy.speak("Woof!"))  # Buddy says Woof!
print(miles.speak("Bow-wow"))  # Miles says Bow-wow
