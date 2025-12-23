#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 10: Practical for Loop Examples
"""

print("=== Print multiplication table ===")
number = 5
for i in range(1, 11):
    print(number, "×", i, "=", number * i)

print("\n=== Calculate sum of numbers 1 to 10 ===")
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)  # 55

print("\n=== Print a pattern ===")
for i in range(1, 6):
    print("*" * i)
# Output:
# *
# **
# ***
# ****
# *****
