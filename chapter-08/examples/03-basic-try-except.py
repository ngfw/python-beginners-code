#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 3: Basic try-except Block

Demonstrates the basic structure of try-except error handling.
"""

print("=== Basic try-except ===")
print("This example simulates user input with a fixed value.\n")

# Simulate user input
user_input = "5"
print(f"Simulated input: {user_input}")

try:
    # Code that might cause an error
    number = int(user_input)
    result = 10 / number
    print(f"Result: {result}")
except:
    # Runs if any error occurs
    print("An error occurred!")

print("\n=== Testing with invalid input ===")
user_input = "abc"
print(f"Simulated input: {user_input}")

try:
    number = int(user_input)
    result = 10 / number
    print(f"Result: {result}")
except:
    print("An error occurred!")
