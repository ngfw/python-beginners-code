#!/usr/bin/env python3

"""
Chapter 8: Error Handling
Exercise 8.2: Safe Calculator

Create a calculator program that handles all potential errors
(division by zero, invalid input, etc.).


TODO: Complete the exercises below
"""

def safe_calculator():
    """A calculator with comprehensive error handling (demo mode)"""
    # TODO: Your code here
    pass

        try:
            result = eval(expression)

# Test cases
# TODO: Uncomment and complete
#             print(f"Result: {result}\n")

        except ZeroDivisionError:

# Test cases
# TODO: Uncomment and complete
#             print("Error: Cannot divide by zero!\n")
        except SyntaxError:

# Test cases
# TODO: Uncomment and complete
#             print("Error: Invalid expression!\n")
        except Exception as e:

# Test cases
# TODO: Uncomment and complete
#             print(f"Error: {e}\n")

# Run the calculator
safe_calculator()