#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 6: Temperature Advisor
"""

temp = int(input("What's the temperature? "))

if temp >= 80:
    print("It's hot! Wear light clothing")
elif temp >= 60:
    print("It's nice! Perfect weather")
elif temp >= 40:
    print("It's cool! Bring a jacket")
else:
    print("It's cold! Bundle up!")
