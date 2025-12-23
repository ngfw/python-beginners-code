#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 13: Encapsulation (Private Attributes)

Demonstrates encapsulation using underscore prefix for "private" attributes.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # "Private" attribute (convention)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance

# Usage
print("=== Encapsulation Demo ===\n")

account = BankAccount("Alice", 1000)

# Should use methods, not direct access
print(f"Balance: ${account.get_balance()}")  # Good: 1000

# Direct access is possible but discouraged
# account._balance = 999999  # Bad: direct modification

account.deposit(500)
print(f"After deposit: ${account.get_balance()}")  # 1500

account.withdraw(200)
print(f"After withdrawal: ${account.get_balance()}")  # 1300
