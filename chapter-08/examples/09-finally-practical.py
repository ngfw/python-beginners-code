#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 9: Practical Use of finally

Demonstrates using finally for timing and cleanup operations.
"""

import time

def process_data():
    """Process data with timing in finally block"""
    print("Starting process...")
    start_time = time.time()

    try:
        # Simulate processing
        result = 10 / 0  # This will fail
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error in calculation!")
    finally:
        # Always measure execution time
        end_time = time.time()
        print(f"Process took {end_time - start_time:.4f} seconds")

print("=== Processing with Error ===")
process_data()

def process_data_success():
    """Process data successfully"""
    print("\nStarting process...")
    start_time = time.time()

    try:
        # Simulate processing
        time.sleep(0.1)  # Simulate work
        result = 10 / 2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error in calculation!")
    finally:
        # Always measure execution time
        end_time = time.time()
        print(f"Process took {end_time - start_time:.4f} seconds")

print("\n=== Processing Successfully ===")
process_data_success()
