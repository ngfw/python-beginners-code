#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Exercise 6.2: Convert to Snake Case

Create a function that converts a string to snake_case.
"""

def to_snake_case(text):
    """Convert text to snake_case"""
    return text.lower().replace(" ", "_")

# Test the function
print(to_snake_case("Hello World"))       # hello_world
print(to_snake_case("Python Is Awesome")) # python_is_awesome
