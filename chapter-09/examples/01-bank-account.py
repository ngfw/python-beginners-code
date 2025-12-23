#!/usr/bin/env python3
"""
Chapter 9: Classes & OOP
Example: Bank Account Class
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > 0:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Invalid withdrawal amount"

    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def show_history(self):
        print(f"\nTransaction History for {self.owner}:")
        for transaction in self.transaction_history:
            print(f"  - {transaction}")

# Test the class
account = BankAccount("Alice", 1000)
print(account.get_balance())

print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))  # Should fail

account.show_history()
