#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 18: Various Import Styles
"""

print("=== Basic import ===")
import math
print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0

print("\n=== Import specific functions ===")
from math import e, factorial
print(e)              # 2.718281828459045
print(factorial(5))   # 120

print("\n=== Import with alias ===")
import random as rnd
print(rnd.randint(1, 10))
