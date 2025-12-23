#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Exercise 4.8: Create a random password generator function generate_password(length) using the random module.
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

# Alternative using join
def generate_password_alt(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

print("Password 1:", generate_password(12))
print("Password 2:", generate_password_alt(12))
