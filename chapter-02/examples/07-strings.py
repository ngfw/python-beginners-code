#!/usr/bin/env python3
"""
Chapter 2: Python Basics
Example 7: Strings (str)
"""

name = "Alice"
city = 'New York'
message = "Hello, World!"
empty = ""

print("name:", name, "- type:", type(name))
print("city:", city, "- type:", type(city))
print("message:", message)
print("empty:", empty, "- type:", type(empty))

# These are identical
text1 = "Hello"
text2 = 'Hello'
print("\ntext1:", text1)
print("text2:", text2)
print("Are they equal?", text1 == text2)

# Use different quotes if your text contains quotes
sentence = "She said, 'Hello!'"
another = 'He replied, "Hi there!"'
print("\n" + sentence)
print(another)
