#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 14: Writing JSON

Demonstrates writing JSON files and converting to JSON strings.
"""

import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"]
}

print("=== Writing to JSON file ===")
# Write to file (formatted)
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("✓ Written to data.json")

# Read to verify
with open("data.json", "r") as file:
    print("\n=== File contents: ===")
    print(file.read())

print("\n=== Converting to JSON string ===")
# Convert to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)
