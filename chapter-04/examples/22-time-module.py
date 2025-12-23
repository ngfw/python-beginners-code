#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 22: time Module Examples
"""

import time

print("=== Pause program ===")
print("Starting...")
time.sleep(2)  # Pause for 2 seconds
print("Done!")

print("\n=== Measure execution time ===")
start = time.time()
# Do something that takes time
total = 0
for i in range(1000000):
    total += i
end = time.time()
print("Execution time:", end - start, "seconds")
