#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 6: Parameter Order Matters
"""

def calculate_rectangle(length, width):
    area = length * width
    print("Area:", area)

calculate_rectangle(10, 5)  # Area: 50
calculate_rectangle(5, 10)  # Area: 50 (same result)

# But order matters for different operations:
def divide(a, b):
    print(a / b)

divide(10, 2)  # 5.0
divide(2, 10)  # 0.2 (different!)
