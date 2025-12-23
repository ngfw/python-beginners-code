#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 15: Global Scope
"""

global_var = 100  # Global variable

def my_function():
    print(global_var)  # Can read global variables

my_function()  # 100
print(global_var)  # 100
