#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 17: Modifying Global Variables
"""

print("=== Using global keyword (not recommended) ===")
count = 0

def increment():
    global count  # Tell Python we're using the global variable
    count += 1

increment()
increment()
print(count)  # 2

print("\n=== Better approach: use parameters and return values ===")
def increment_better(value):
    return value + 1

count = 0
count = increment_better(count)
count = increment_better(count)
print(count)  # 2
