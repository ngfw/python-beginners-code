#!/usr/bin/env python3
"""
Chapter 10: Python Projects for Beginners
Project 1: Calculator with History

A complete calculator that performs operations and keeps a history of calculations.
"""

import datetime

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            self._add_to_history(f"{a} ÷ {b} = Error: Division by zero")
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
        return result

    def power(self, base, exp):
        result = base ** exp
        self._add_to_history(f"{base} ^ {exp} = {result}")
        return result

    def _add_to_history(self, calculation):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.history.append(f"[{timestamp}] {calculation}")

    def show_history(self):
        if not self.history:
            print("No calculations yet!")
            return

        print("\n=== Calculation History ===")
        for entry in self.history:
            print(entry)

    def clear_history(self):
        self.history = []
        print("History cleared!")

def main():
    """Demo mode - automatically tests calculator features"""
    calc = Calculator()
    
    print("=== Calculator Demo ===\n")
    
    # Demonstrate various operations
    print("Performing calculations...")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"20 - 8 = {calc.subtract(20, 8)}")
    print(f"6 × 7 = {calc.multiply(6, 7)}")
    print(f"100 ÷ 4 = {calc.divide(100, 4)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    
    # Show history
    calc.show_history()
    
    # Test error handling
    print("\n=== Testing Error Handling ===")
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Caught error: {e}")
    
    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    main()
