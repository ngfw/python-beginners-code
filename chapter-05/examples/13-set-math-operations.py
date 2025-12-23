#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 13: Set Mathematical Operations
"""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Union (all items from both sets)
print("\n=== Union ===")
print("set1 | set2:", set1 | set2)
print("set1.union(set2):", set1.union(set2))

# Intersection (items in both sets)
print("\n=== Intersection ===")
print("set1 & set2:", set1 & set2)
print("set1.intersection(set2):", set1.intersection(set2))

# Difference (items in set1 but not set2)
print("\n=== Difference ===")
print("set1 - set2:", set1 - set2)
print("set1.difference(set2):", set1.difference(set2))

# Symmetric difference (items in one set but not both)
print("\n=== Symmetric Difference ===")
print("set1 ^ set2:", set1 ^ set2)
print("set1.symmetric_difference(set2):", set1.symmetric_difference(set2))
