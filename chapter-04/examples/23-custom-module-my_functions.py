#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 23: Creating Your Own Module
This is my_functions.py
"""

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159

# Test the module
if __name__ == "__main__":
    print(greet("Alice"))
    print("5 + 3 =", add(5, 3))
    print("5 * 3 =", multiply(5, 3))
    print("PI =", PI)
