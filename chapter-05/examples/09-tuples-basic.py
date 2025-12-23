#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 9: Creating Tuples
"""

# Empty tuple
empty = ()
print("Empty tuple:", empty)

# Tuple with parentheses
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Tuple without parentheses (tuple packing)
point = 5, 10, 15
print("Point:", point)

# Single-item tuple (note the comma!)
single = (42,)  # Without comma, it's just a number
print("Single-item tuple:", single)
print("Type:", type(single))

# Multiple types
mixed = (1, "hello", 3.14)
print("Mixed tuple:", mixed)
