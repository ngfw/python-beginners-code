#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Example 14: Logical Operators
"""

print("=== Logical Operators ===")

# AND - both must be True
print("True and True:", True and True)  # True
print("True and False:", True and False)  # False
print("False and False:", False and False)  # False

# OR - at least one must be True
print("True or False:", True or False)  # True
print("False or False:", False or False)  # False
print("True or True:", True or True)  # True

# NOT - inverts the boolean
print("not True:", not True)  # False
print("not False:", not False)  # True

print("\n=== Practical Examples ===")

age = 25
has_license = True

# Can rent a car if age >= 21 AND has license
can_rent_car = age >= 21 and has_license
print("Can rent car:", can_rent_car)  # True

# Gets discount if student OR senior
is_student = False
is_senior = True
gets_discount = is_student or is_senior
print("Gets discount:", gets_discount)  # True
