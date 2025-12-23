#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 14: break Statement
"""

print("=== Stop when we find the number ===")
for i in range(1, 11):
    print(i)
    if i == 5:
        print("Found 5! Stopping...")
        break

print("\n=== Practical example: Search ===")
numbers = [10, 25, 30, 45, 50]
search_for = 30
found = False

for num in numbers:
    if num == search_for:
        print("Found", search_for)
        found = True
        break

if not found:
    print(search_for, "not found")
