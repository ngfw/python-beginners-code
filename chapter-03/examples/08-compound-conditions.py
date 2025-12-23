#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 8: Compound Conditions (AND, OR, NOT)
"""

print("=== Using AND ===")
age = 25
income = 50000

if age >= 21 and income >= 30000:
    print("You qualify for the loan")

print("\n=== Using OR ===")
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

print("\n=== Using NOT ===")
is_raining = False

if not is_raining:
    print("You don't need an umbrella")

print("\n=== Complex Example ===")
age = 20
has_id = True
has_ticket = True

if age >= 18 and has_id and has_ticket:
    print("You can enter the concert")
elif age >= 18 and has_id:
    print("You need to buy a ticket")
elif age >= 18:
    print("You need to show ID and buy a ticket")
else:
    print("Sorry, you must be 18 or older")
