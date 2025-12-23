#!/usr/bin/env python3
"""
Chapter 8: Error Handling
Exercise 8.2: Safe Calculator

Create a calculator program that handles all potential errors
(division by zero, invalid input, etc.).
"""

def safe_calculator():
    """A calculator with comprehensive error handling (demo mode)"""
    # Demo mode - simulate user inputs
    test_expressions = [
        "2 + 2",
        "10 / 2",
        "10 / 0",
        "invalid",
        "5 * 3",
        "quit"
    ]
    
    print("=== Safe Calculator (Demo Mode) ===")
    print("Testing various expressions...\n")
    
    for expression in test_expressions:
        print(f"Expression: {expression}")
        
        if expression.lower() == 'quit':
            print("Goodbye!\n")
            break

        try:
            result = eval(expression)
            print(f"Result: {result}\n")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero!\n")
        except SyntaxError:
            print("Error: Invalid expression!\n")
        except Exception as e:
            print(f"Error: {e}\n")

# Run the calculator
safe_calculator()
