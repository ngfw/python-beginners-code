#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 9: Basic for Loop with range()
"""

print("=== Basic for loop ===")
for i in range(5):
    print("Hello!")

print("\n=== range(stop) - counts from 0 to stop-1 ===")
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

print("\n=== range(start, stop) - counts from start to stop-1 ===")
for i in range(2, 6):
    print(i)
# Output: 2, 3, 4, 5

print("\n=== range(start, stop, step) - counts with custom increment ===")
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

print("\n=== Counting backwards ===")
for i in range(10, 0, -1):
    print(i)
# Output: 10, 9, 8, ..., 1
