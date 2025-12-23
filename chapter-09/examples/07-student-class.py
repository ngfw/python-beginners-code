#!/usr/bin/env python3
"""
Chapter 9: Classes & Object-Oriented Programming
Example 7: Student Class

Demonstrates a Student class with grade management.
"""

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade! Must be between 0 and 100")

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id})"

# Usage
print("=== Student Class Demo ===\n")
student = Student("Alice", "S12345")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)

print(student)  # Student: Alice (ID: S12345)
print(f"Average: {student.get_average():.2f}")  # Average: 85.00
print(f"Letter Grade: {student.get_letter_grade()}")  # Letter Grade: B
