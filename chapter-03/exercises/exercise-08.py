#!/usr/bin/env python3

"""
Chapter 3: Control Flow
Exercise 3.8: Create a simple menu system:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Keep showing the menu until the user chooses Exit.


TODO: Complete the exercises below
"""

while True:

# Test cases
# TODO: Uncomment and complete
#     print("\n=== Calculator Menu ===")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":

# Test cases
# TODO: Uncomment and complete
#         print("Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":

# Test cases
# TODO: Uncomment and complete
#             print("Result:", num1 + num2)
        elif choice == "2":

# Test cases
# TODO: Uncomment and complete
#             print("Result:", num1 - num2)
        elif choice == "3":

# Test cases
# TODO: Uncomment and complete
#             print("Result:", num1 * num2)
        elif choice == "4":
            if num2 != 0:

# Test cases
# TODO: Uncomment and complete
#                 print("Result:", num1 / num2)
            else:

# Test cases
# TODO: Uncomment and complete
#                 print("Error: Cannot divide by zero")
    else:

# Test cases
# TODO: Uncomment and complete
#         print("Invalid choice!")