#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Example 20: Calculator with Error Handling

Demonstrates a calculator class with comprehensive error handling.
"""

class Calculator:
    def divide(self, a, b):
        """Divide two numbers with error handling"""
        try:
            return a / b
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
        except TypeError:
            raise TypeError("Both arguments must be numbers")

    def sqrt(self, n):
        """Calculate square root with validation"""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return n ** 0.5

    def calculate(self, expression):
        """Safely evaluate mathematical expression"""
        try:
            # Note: eval() can be dangerous in production, use with caution
            result = eval(expression)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception as e:
            return f"Error: Invalid expression ({e})"

# Usage
print("=== Calculator Demo ===\n")
calc = Calculator()

# Test divide
print("Test 1: divide(10, 2)")
try:
    print(f"  Result: {calc.divide(10, 2)}")   # 5.0
except ValueError as e:
    print(f"  Error: {e}")

print("\nTest 2: divide(10, 0)")
try:
    print(f"  Result: {calc.divide(10, 0)}")   # Raises ValueError
except ValueError as e:
    print(f"  Error: {e}")

# Test sqrt
print("\nTest 3: sqrt(16)")
try:
    print(f"  Result: {calc.sqrt(16)}")   # 4.0
except ValueError as e:
    print(f"  Error: {e}")

print("\nTest 4: sqrt(-4)")
try:
    print(f"  Result: {calc.sqrt(-4)}")   # Raises ValueError
except ValueError as e:
    print(f"  Error: {e}")

# Test calculate
print("\nTest 5: calculate('2 + 2')")
print(f"  Result: {calc.calculate('2 + 2')}")

print("\nTest 6: calculate('10 / 0')")
print(f"  Result: {calc.calculate('10 / 0')}")
