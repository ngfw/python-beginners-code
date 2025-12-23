#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 9: Return Values
"""

def add(a, b):
    result = a + b
    return result

answer = add(5, 3)
print(answer)  # 8

print("\n=== Without return, functions return None ===")

def greet(name):
    print("Hello,", name)

result = greet("Alice")
print("Result:", result)  # None
