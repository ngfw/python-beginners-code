# Chapter 8: Error Handling

## 📚 Learning Objectives

By the end of this chapter, you will be able to:
- Understand different types of errors (syntax vs runtime)
- Use try-except blocks to handle exceptions gracefully
- Handle multiple exceptions with different responses
- Use else and finally clauses effectively
- Raise your own exceptions when needed
- Create custom exception classes
- Apply best practices for error handling
- Write robust, production-ready code

## 📂 Directory Structure

- **examples/** - Working code examples from the chapter
- **exercises/** - Practice exercises for you to complete
  - **solutions/** - Full solutions (try exercises first!)

## 🎯 What You'll Learn

Errors are inevitable in programming. This chapter teaches you to anticipate, catch, and handle errors gracefully instead of letting your program crash. You'll learn to write defensive code that handles edge cases and provides helpful error messages to users.

## 📝 Examples

- **01-syntax-errors.py** - Common syntax error examples
- **02-runtime-errors.py** - Exceptions that occur during execution
- **03-basic-try-except.py** - Your first try-except block
- **04-specific-exceptions.py** - Catching specific error types
- **05-error-details.py** - Getting error information
- **06-multiple-exceptions.py** - Handling different exceptions differently
- **07-else-clause.py** - Code that runs when no error occurs
- **08-finally-clause.py** - Code that always runs
- **09-finally-practical.py** - Practical finally usage
- **10-raising-exceptions.py** - Raising your own exceptions
- **11-validating-input.py** - Input validation with exceptions
- **12-reraising-exceptions.py** - Re-raising caught exceptions
- **13-custom-exceptions.py** - Creating custom exception classes
- **14-best-practice-specific.py** - Being specific with exceptions
- **15-best-practice-dont-hide.py** - Don't hide errors silently
- **16-best-practice-exceptional-cases.py** - Use exceptions correctly
- **17-best-practice-useful-messages.py** - Providing helpful error messages
- **18-safe-input-function.py** - Robust input handling
- **19-file-operations-with-errors.py** - Safe file operations
- **20-calculator-with-errors.py** - Complete error-handled calculator
- **21-debug-information.py** - Printing debug info
- **22-using-assertions.py** - Development-time checks

## ✏️ Exercises

- **exercise-01.py** - Create safe_int() function that never crashes
- **exercise-02.py** - Build a calculator with comprehensive error handling

## 🚀 How to Use

1. Read Chapter 8 in the book
2. Run the examples: `python3 examples/03-basic-try-except.py`
3. Try the exercises: `python3 exercises/exercise-01.py`
4. Check solutions only after attempting: `python3 exercises/solutions/exercise-01-safe-int.py`

## 💡 Tips

- Be specific with exceptions - catch ValueError, not Exception
- Never use bare `except:` - it catches everything including Ctrl+C!
- Use `finally` for cleanup code that must run (like closing files)
- `else` runs only if no exception occurred
- Don't use exceptions for normal program flow - they're for exceptional cases
- Provide helpful error messages: "Age must be 0-150, got -5" not just "Error!"
- Read error messages carefully - they tell you exactly what went wrong
- Test your error handling by intentionally causing errors

---

**Previous**: [Chapter 7 - File I/O](../chapter-07/) | **Next**: [Chapter 9 - Classes & OOP](../chapter-09/)
