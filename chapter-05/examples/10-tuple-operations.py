#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 10: Tuple Operations
"""

print("=== Accessing elements ===")
coordinates = (10, 20, 30)
print("First:", coordinates[0])   # 10
print("Last:", coordinates[-1])  # 30
print("Slice:", coordinates[1:])  # (20, 30)

print("\n=== Tuple unpacking ===")
def get_coordinates():
    return 10, 20  # Returns a tuple

x, y = get_coordinates()  # Tuple unpacking
print("x:", x, "y:", y)  # 10 20

print("\n=== Tuple operations ===")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print("Combined:", combined)  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 3
print("Repeated:", repeated)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Length
print("Length:", len(tuple1))  # 3

# Count
numbers = (1, 2, 2, 3, 2)
print("Count of 2:", numbers.count(2))  # 3

# Index
print("Index of 3:", numbers.index(3))  # 3
