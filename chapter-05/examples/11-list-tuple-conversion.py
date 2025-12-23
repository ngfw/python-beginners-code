#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Example 11: Converting Between Lists and Tuples
"""

print("=== List to tuple ===")
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("List:", my_list)
print("Tuple:", my_tuple)

print("\n=== Tuple to list ===")
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print("Tuple:", my_tuple)
print("List:", my_list)
