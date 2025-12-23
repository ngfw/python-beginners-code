#!/usr/bin/env python3

"""
Chapter 5: Data Structures
Exercise 5.6: Merge two dictionaries into one.


TODO: Complete the exercises below
"""

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Test cases
# TODO: Uncomment and complete
# print("Dict 1:", dict1)
# print("Dict 2:", dict2)

# Test cases
# TODO: Uncomment and complete
# print("\n=== Method 1: update() ===")
merged = dict1.copy()
merged.update(dict2)

# Test cases
# TODO: Uncomment and complete
# print("Merged:", merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Test cases
# TODO: Uncomment and complete
# print("\n=== Method 2: unpacking (Python 3.5+) ===")
merged = {**dict1, **dict2}

# Test cases
# TODO: Uncomment and complete
# print("Merged:", merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}