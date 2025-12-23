#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 14: Property Decorators

Demonstrates using @property for controlled attribute access.
"""

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

# Usage
print("=== Property Decorators Demo ===\n")

temp = Temperature(25)
print(f"Celsius: {temp.celsius}")     # 25
print(f"Fahrenheit: {temp.fahrenheit}")  # 77.0

print("\nSetting Fahrenheit to 98.6...")
temp.fahrenheit = 98.6
print(f"Celsius: {temp.celsius:.1f}")     # 37.0
print(f"Fahrenheit: {temp.fahrenheit}")  # 98.6

print("\nTrying to set temperature below absolute zero...")
try:
    temp.celsius = -300  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
