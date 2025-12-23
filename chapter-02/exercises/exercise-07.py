#!/usr/bin/env python3

"""
Chapter 2: Python Basics
Exercise 2.7: Ask user for their age and whether they have a license.
Print True/False if they can drive (age >= 16 and has license).


TODO: Complete the exercises below
"""

age = int(input("Enter your age: "))
has_license_input = input("Do you have a license? (yes/no): ")
has_license = has_license_input.lower() == "yes"

can_drive = age >= 16 and has_license

# Test cases
# TODO: Uncomment and complete
# print("Can drive:", can_drive)