#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 5: Password Checker
"""

password = input("Enter password: ")

if len(password) < 8:
    print("Password too short! Must be at least 8 characters")
else:
    print("Password accepted")
