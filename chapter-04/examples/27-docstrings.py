#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 27: Function Documentation (Docstrings)
"""

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The area of the rectangle
    """
    return length * width

# Use the function
area = calculate_area(10, 5)
print(f"Area: {area}")

# Access docstring
print("\nDocstring:")
print(calculate_area.__doc__)

print("\nUsing help():")
help(calculate_area)
