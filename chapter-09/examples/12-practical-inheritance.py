#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 12: Practical Inheritance Example

Demonstrates inheritance with Employee, Manager, and Developer classes.
"""

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
        self.team = []

    def add_team_member(self, employee):
        self.team.append(employee)

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print(f"Team Size: {len(self.team)}")

class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_languages):
        super().__init__(name, emp_id, salary)
        self.programming_languages = programming_languages

    def display_info(self):
        super().display_info()
        print(f"Languages: {', '.join(self.programming_languages)}")

# Usage
print("=== Employee Management System ===\n")

manager = Manager("Alice", "M001", 80000, "Engineering")
dev1 = Developer("Bob", "D001", 70000, ["Python", "JavaScript"])
dev2 = Developer("Charlie", "D002", 75000, ["Python", "Go"])

manager.add_team_member(dev1)
manager.add_team_member(dev2)

print("=== Manager Info ===")
manager.display_info()

print("\n=== Developer Info ===")
dev1.display_info()
