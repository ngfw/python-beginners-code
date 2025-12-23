#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 16: break vs continue Comparison
"""

print("=== break: Exits the entire loop ===")
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0, 1, 2

print("\n=== continue: Skips to next iteration ===")
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0, 1, 2, 4 (skips 3)
