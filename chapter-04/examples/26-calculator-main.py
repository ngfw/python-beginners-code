#!/usr/bin/env python3
"""
Chapter 4: Functions & Modules
Example 26: Calculator Main Program
This uses the calculator module.

Note: For standalone testing, calculator functions are defined inline.
"""

# Calculator functions (normally imported from calculator.py)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(base, exponent):
    return base ** exponent

def percentage(value, percent):
    return (value * percent) / 100

def show_menu():
    print("\n=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Percentage")
    print("7. Exit")

# Main program
while True:
    show_menu()
    choice = input("\nEnter your choice (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice in ["1", "2", "3", "4", "5", "6"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        elif choice == "5":
            result = power(a, b)
        elif choice == "6":
            result = percentage(a, b)

        print(f"Result: {result}")
    else:
        print("Invalid choice!")
