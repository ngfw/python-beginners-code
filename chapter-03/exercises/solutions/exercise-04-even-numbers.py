#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Exercise 3.4: Create a program that prints all even numbers from 1 to 50.
"""

for i in range(2, 51, 2):
    print(i)

# Alternative:
print("\n=== Alternative method ===")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
