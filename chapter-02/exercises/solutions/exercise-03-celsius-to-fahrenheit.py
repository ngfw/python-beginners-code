#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Exercise 2.3: Convert Celsius to Fahrenheit
Formula: F = (C × 9/5) + 32
"""

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "°C =", fahrenheit, "°F")
