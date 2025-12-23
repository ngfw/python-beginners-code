#!/usr/bin/env python3
"""
Chapter 10: Python Projects for Beginners
Project 2: To-Do List Application

A complete task management app with file persistence.
"""

import json
import datetime
from pathlib import Path

class Task:
    def __init__(self, title, description="", priority="medium"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.datetime.now().isoformat()
        self.completed_at = None

    def mark_complete(self):
        self.completed = True
        self.completed_at = datetime.datetime.now().isoformat()

    def mark_incomplete(self):
        self.completed = False
        self.completed_at = None

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["description"], data["priority"])
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        task.completed_at = data["completed_at"]
        return task

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description="", priority="medium"):
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Added task: {title}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            self.save_tasks()
            print(f"✓ Removed task: {task.title}")
        else:
            print("✗ Invalid task number!")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            self.save_tasks()
            print(f"✓ Completed: {self.tasks[index].title}")
        else:
            print("✗ Invalid task number!")

    def list_tasks(self, show_completed=True):
        if not self.tasks:
            print("\nNo tasks yet! Add some tasks to get started.")
            return

        print("\n=== Your Tasks ===")

        for i, task in enumerate(self.tasks):
            if not show_completed and task.completed:
                continue

            status = "✓" if task.completed else "○"
            priority_symbol = {"high": "!", "medium": "-", "low": "·"}[task.priority]

            print(f"\n{i+1}. [{status}] {priority_symbol} {task.title}")

            if task.description:
                print(f"   {task.description}")

            created = datetime.datetime.fromisoformat(task.created_at)
            print(f"   Created: {created.strftime('%Y-%m-%d %H:%M')}")

            if task.completed and task.completed_at:
                completed = datetime.datetime.fromisoformat(task.completed_at)
                print(f"   Completed: {completed.strftime('%Y-%m-%d %H:%M')}")

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except FileNotFoundError:
            self.tasks = []

def main():
    """Demo mode - automatically creates and manages tasks"""
    print("=== To-Do List Demo ===\n")
    
    todo = TodoList("demo_tasks.json")
    
    # Add some demo tasks
    print("Adding demo tasks...")
    todo.add_task("Learn Python basics", "Complete Chapter 1-5", "high")
    todo.add_task("Build a project", "Create a calculator app", "medium")
    todo.add_task("Practice coding", "Solve coding challenges", "low")
    
    # List all tasks
    todo.list_tasks()
    
    # Complete a task
    print("\n=== Completing first task ===")
    todo.complete_task(0)
    
    # List tasks again
    todo.list_tasks()
    
    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    main()
