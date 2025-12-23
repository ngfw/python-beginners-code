#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Exercise 2.5: Write a program that asks for a price and calculates:
- 15% tip
- 20% tip
- Total with each tip
"""

price = float(input("Enter price: $"))

tip_15 = price * 0.15
tip_20 = price * 0.20

total_15 = price + tip_15
total_20 = price + tip_20

print("15% tip: $", tip_15, " - Total: $", total_15)
print("20% tip: $", tip_20, " - Total: $", total_20)
