#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 4: Nested if Statements
"""

age = 20
has_license = True

if age >= 18:
    print("You are old enough to drive")
    if has_license:
        print("You can drive!")
    else:
        print("But you need a license first")
else:
    print("You are too young to drive")
