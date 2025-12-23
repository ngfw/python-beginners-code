#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Exercise 4.5: Check if a number is prime
"""

def is_prime(number):
    """Check if a number is prime"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
print(is_prime(17))  # True
print(is_prime(10))  # False
print(is_prime(2))   # True
print(is_prime(1))   # False
