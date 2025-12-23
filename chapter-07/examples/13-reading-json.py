#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 13: Reading JSON

Demonstrates reading JSON files and parsing JSON strings.
"""

import json

# Create a sample JSON file
data = {"name": "Alice", "age": 25, "city": "New York"}
with open("data.json", "w") as f:
    json.dump(data, f)

print("=== Reading JSON file ===")
# Read JSON file
with open("data.json", "r") as file:
    data = json.load(file)
    print(f"Loaded data: {data}")
    print(f"Name: {data['name']}")

print("\n=== Parsing JSON string ===")
# Parse JSON string
json_string = '{"name": "Alice", "age": 25, "city": "New York"}'
data = json.loads(json_string)
print(f"Parsed data: {data}")
print(f"Name: {data['name']}")  # Alice
