#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 17: Nested Loops
"""

print("=== Multiplication table ===")
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")  # \t is tab
    print()  # New line after each row

print("\n=== Right triangle ===")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print("\n=== Square ===")
size = 5
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()
