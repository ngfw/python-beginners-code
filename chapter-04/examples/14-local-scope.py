#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 14: Local Scope
"""

def my_function():
    local_var = 10  # Local variable
    print(local_var)

my_function()  # 10

# This would cause an error:
# print(local_var)  # Error! local_var doesn't exist outside function
print("(local_var is not accessible here)")
