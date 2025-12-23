#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 24: Using Custom Module
This is main.py that imports my_functions.py

Note: This example requires my_functions.py to be in the same directory.
For testing purposes, we'll use inline import simulation.
"""

# In a real scenario, you would do:
# import my_functions
# print(my_functions.greet("Alice"))
# print(my_functions.add(5, 3))
# print(my_functions.PI)

# For this standalone example, we'll define the functions here
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159

# Use the functions
print(greet("Alice"))
print("5 + 3 =", add(5, 3))
print("PI =", PI)
