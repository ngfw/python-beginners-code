#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 16: Local vs Global Variables
"""

x = 10  # Global

def test():
    x = 20  # Local (different from global x)
    print("Inside function:", x)

test()  # Inside function: 20
print("Outside function:", x)  # Outside function: 10
