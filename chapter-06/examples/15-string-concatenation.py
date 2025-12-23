#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 15: String Concatenation

Demonstrates different methods of concatenating strings:
- + operator
- join() method (more efficient for many strings)
- f-strings
- Performance considerations
"""

# Using + operator
first = "Hello"
last = "World"
full = first + " " + last
print(f"Using +: {full}")  # Hello World

# Using join (more efficient for many strings)
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"Using join: {sentence}")  # Python is awesome

# Using f-strings
name = "Alice"
greeting = f"Hello, {name}!"
print(f"Using f-string: {greeting}")  # Hello, Alice!

# Performance comparison note
print("\n=== Performance Note ===")
print("For many concatenations, join() is faster than +=")

# Inefficient (commented out for brevity)
# result = ""
# for i in range(1000):
#     result += str(i)  # Slow!

# Efficient
numbers = [str(i) for i in range(10)]
result = "".join(numbers)  # Fast!
print(f"Joined numbers (0-9): {result}")
