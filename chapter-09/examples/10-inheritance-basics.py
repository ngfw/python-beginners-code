#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 10: Inheritance Basics

Demonstrates basic inheritance with Animal, Dog, and Cat classes.
"""

# Parent class (base class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

    def info(self):
        return f"I am {self.name}"

# Child class (derived class)
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage
print("=== Inheritance Demo ===\n")

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.info())   # I am Buddy (inherited from Animal)
print(dog.speak())  # Woof! (overridden in Dog)

print()

print(cat.info())   # I am Whiskers (inherited)
print(cat.speak())  # Meow! (overridden in Cat)
