#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 11: Extending Parent Class

Demonstrates using super() to call parent class methods.
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed

    def info(self):
        # Extend parent method
        base_info = super().info()
        return f"{base_info} and is a {self.breed}"

# Usage
print("=== Extending Parent Class Demo ===\n")

dog = Dog("Buddy", 3, "Golden Retriever")
print(dog.info())  # Buddy is 3 years old and is a Golden Retriever
