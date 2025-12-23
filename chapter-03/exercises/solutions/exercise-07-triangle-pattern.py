#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Exercise 3.7: Write a program that prints a triangle pattern:
    *
   ***
  *****
 *******
*********
"""

rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()
