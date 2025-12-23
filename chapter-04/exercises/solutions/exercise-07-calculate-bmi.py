#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Exercise 4.7: Write a function calculate_bmi(weight, height) that calculates Body Mass Index.
(BMI = weight / height²)
"""

def calculate_bmi(weight, height):
    """
    Calculate BMI
    weight: in kilograms
    height: in meters
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)

print(calculate_bmi(70, 1.75))  # 22.86
