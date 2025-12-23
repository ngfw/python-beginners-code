# Chapter 9: Classes & Object-Oriented Programming

## 📚 Learning Objectives

By the end of this chapter, you will be able to:
- Create classes and objects (instances)
- Use attributes to store object properties
- Define methods to give objects behaviors
- Understand and use the `__init__` constructor
- Work with class attributes vs instance attributes
- Implement inheritance to reuse code
- Apply encapsulation principles with private attributes
- Use property decorators for controlled access
- Build practical OOP applications

## 📂 Directory Structure

- **examples/** - Working code examples from the chapter
- **exercises/** - Practice exercises for you to complete
  - **solutions/** - Full solutions (try exercises first!)

## 🎯 What You'll Learn

Object-Oriented Programming (OOP) is a powerful way to organize code that mirrors the real world. This chapter introduces classes and objects, teaching you to create reusable, organized code. You'll learn to model real-world entities like bank accounts, students, and library systems using OOP principles.

## 📝 Examples

- **01-basic-class.py** - Creating your first class
- **02-class-attributes.py** - Shared attributes across instances
- **03-adding-methods.py** - Giving classes behaviors
- **04-init-constructor.py** - Initializing objects with __init__
- **05-instance-vs-class-attributes.py** - Understanding attribute types
- **06-bank-account-class.py** - Practical bank account example
- **07-student-class.py** - Student with grades tracking
- **08-rectangle-class.py** - Geometric shapes with OOP
- **09-special-methods.py** - Magic methods (__str__, __repr__, etc.)
- **10-inheritance-basics.py** - Creating child classes
- **11-extending-parent-class.py** - Using super() to extend functionality
- **12-practical-inheritance.py** - Employee hierarchy example
- **13-encapsulation.py** - Private attributes with underscore
- **14-property-decorators.py** - Using @property for getters/setters
- **15-library-system.py** - Complete library management system

## ✏️ Exercises

- **exercise-01.py** - Create a Car class with attributes and methods
- **exercise-02.py** - Build a Circle class with area/circumference calculations
- **exercise-03.py** - Implement a TodoList class for task management
- **exercise-04.py** - Create Person and Student classes with inheritance
- **exercise-05.py** - Build an inventory system with Product and Inventory classes

## 🚀 How to Use

1. Read Chapter 9 in the book
2. Run the examples: `python3 examples/04-init-constructor.py`
3. Try the exercises: `python3 exercises/exercise-01.py`
4. Check solutions when ready (note: some exercises may not have solution files)

## 💡 Tips

- Class names use PascalCase (BankAccount, StudentRecord)
- Method names use snake_case (get_balance, add_grade)
- `self` refers to the instance and is always the first parameter
- `__init__` runs automatically when you create a new object
- Use `super()` to call parent class methods in inheritance
- Single underscore (_attribute) indicates "private" by convention
- Double underscore (__attribute) triggers name mangling for stricter privacy
- @property makes methods act like attributes for clean syntax
- Keep methods focused - each should do one thing well

---

**Previous**: [Chapter 8 - Error Handling](../chapter-08/) | **Next**: [Chapter 10 - Python Projects](../chapter-10/)
