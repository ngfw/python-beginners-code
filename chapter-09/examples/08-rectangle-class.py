#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 8: Rectangle Class

Demonstrates a Rectangle class with geometric calculations.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width

    def __str__(self):
        return f"Rectangle({self.length}x{self.width})"

# Usage
print("=== Rectangle Class Demo ===\n")

rect = Rectangle(5, 3)
print(rect)  # Rectangle(5x3)
print(f"Area: {rect.area()}")  # Area: 15
print(f"Perimeter: {rect.perimeter()}")  # Perimeter: 16
print(f"Is square? {rect.is_square()}")  # Is square? False

print()

square = Rectangle(4, 4)
print(square)  # Rectangle(4x4)
print(f"Is square? {square.is_square()}")  # Is square? True
