#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 12: Returning Multiple Values
"""

def get_user_info():
    name = "Alice"
    age = 25
    city = "Boston"
    return name, age, city

# Unpack the returned values
user_name, user_age, user_city = get_user_info()
print(user_name)  # Alice
print(user_age)   # 25
print(user_city)  # Boston

print("\n=== Calculate multiple statistics ===")

def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum

data = [10, 20, 30, 40, 50]
sum_val, avg_val, min_val, max_val = calculate_stats(data)

print(f"Sum: {sum_val}")
print(f"Average: {avg_val}")
print(f"Min: {min_val}")
print(f"Max: {max_val}")
