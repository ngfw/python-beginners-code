#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Example 15: Comments and Code Style
"""

# This is a single-line comment

# Calculate the area of a circle
radius = 5
pi = 3.14159
area = pi * radius ** 2  # pi * r^2
print("Area of circle:", area)

"""
This is a multi-line comment.
You can write multiple lines
to explain complex code.
"""

'''
Single or triple quotes work
for multi-line comments.
'''

# Bad comment (obvious)
age = 25  # Set age to 25

# Good comment (explains why)
min_rental_age = 25  # Minimum age for rental car insurance

print("\n=== Code Style Best Practices ===")

# Good - use spaces around operators
x = 10 + 5
print("x =", x)

# Good - one statement per line
x = 5
y = 10
print("x =", x, "y =", y)

# Good - use blank lines to separate logical sections
# Calculate rectangle area
length = 10
width = 5
area = length * width
print("Rectangle area:", area)

# Calculate perimeter
perimeter = 2 * (length + width)
print("Rectangle perimeter:", perimeter)

# If a line is too long, break it
total = (100 + 200 +
         300 + 400)
print("Total:", total)
