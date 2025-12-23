#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 10: Reading CSV Files

Demonstrates reading CSV files using the csv module.
"""

import csv

# Create a sample CSV file
with open("data.csv", "w") as f:
    f.write("name,age,city\n")
    f.write("Alice,25,New York\n")
    f.write("Bob,30,Los Angeles\n")
    f.write("Charlie,35,Chicago\n")

print("=== Method 1: Reading CSV ===")
# Reading CSV
with open("data.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)  # Each row is a list

print("\n=== Method 2: Skip header ===")
# Skip header row
with open("data.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        print(row)

print("\n=== Method 3: Reading as dictionary ===")
# Reading as dictionary (column names as keys)
with open("data.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"{row['name']} is {row['age']} years old")
