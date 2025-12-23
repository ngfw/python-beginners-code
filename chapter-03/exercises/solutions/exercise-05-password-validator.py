#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Exercise 3.5: Write a password validator that keeps asking for a password until the user enters "python123".
"""

password = ""

while password != "python123":
    password = input("Enter the password: ")
    if password != "python123":
        print("Incorrect! Try again")

print("Access granted!")
