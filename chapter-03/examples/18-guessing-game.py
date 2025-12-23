#!/usr/bin/env python3
"""
Chapter 3: Control Flow
Example 18: Complete Number Guessing Game Project
"""

import random

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100")
print()

# Generate random number
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    # Get user guess
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Check guess
    if guess == secret_number:
        print("🎉 Congratulations! You guessed it!")
        print("It took you", attempts, "attempts")
        break
    elif guess < secret_number:
        print("Too low! Try again")
    else:
        print("Too high! Try again")

    # Show remaining attempts
    remaining = max_attempts - attempts
    if remaining > 0:
        print("Attempts remaining:", remaining)
        print()
    else:
        print("Game Over! The number was", secret_number)
