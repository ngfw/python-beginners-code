#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Exercise 2.4: Create a program that calculates the area and perimeter of a rectangle from user input.
"""

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)
