#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 13: Practical while Loop Examples
"""

print("=== Guessing game ===")
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("Correct! You win!")

print("\n=== Countdown ===")
countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Blast off! 🚀")

print("\n=== Keep asking until valid input ===")
age = -1

while age < 0:
    age = int(input("Enter your age (must be positive): "))
    if age < 0:
        print("Invalid! Age cannot be negative")

print("Your age is:", age)
