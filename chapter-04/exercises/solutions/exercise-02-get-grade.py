#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Exercise 4.2: Create a function get_grade(score) that returns a letter grade based on a numeric score.
(A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60)
"""

def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print(get_grade(95))  # A
print(get_grade(82))  # B
print(get_grade(55))  # F
