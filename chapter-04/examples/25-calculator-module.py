#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 25: Simple Calculator Module
This is calculator.py
Contains basic math operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(base, exponent):
    """Raise base to the power of exponent"""
    return base ** exponent

def percentage(value, percent):
    """Calculate percentage of a value"""
    return (value * percent) / 100

def show_menu():
    """Display calculator menu"""
    print("\n=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Percentage")
    print("7. Exit")

# Test the module
if __name__ == "__main__":
    print("Testing calculator module:")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))
    print("2 ^ 3 =", power(2, 3))
    print("20% of 100 =", percentage(100, 20))
    show_menu()
