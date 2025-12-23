#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 20: random Module Examples
"""

import random

print("=== Random integer ===")
print("randint(1, 10):", random.randint(1, 10))

print("\n=== Random float ===")
print("random():", random.random())

print("\n=== Random choice from a list ===")
colors = ["red", "blue", "green", "yellow"]
print("choice(colors):", random.choice(colors))

print("\n=== Shuffle a list ===")
numbers = [1, 2, 3, 4, 5]
print("Before shuffle:", numbers)
random.shuffle(numbers)
print("After shuffle:", numbers)
