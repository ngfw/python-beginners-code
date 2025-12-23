#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 11: Writing CSV Files

Demonstrates writing CSV files using the csv module.
"""

import csv

print("=== Method 1: Writing CSV with writer ===")
# Writing CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

with open("output.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

print("✓ Written to output.csv")

print("\n=== Method 2: Writing with DictWriter ===")
# Writing with dictionary
data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"}
]

with open("output_dict.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    csv_writer.writeheader()  # Write column names
    csv_writer.writerows(data)

print("✓ Written to output_dict.csv")

# Read to verify
print("\n=== Verifying output.csv: ===")
with open("output.csv", "r") as file:
    print(file.read())
