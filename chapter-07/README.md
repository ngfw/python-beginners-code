# Chapter 7: File I/O

## 📚 Learning Objectives

By the end of this chapter, you will be able to:
- Read from and write to text files
- Use the `with` statement for automatic file closing
- Work with file paths using os and pathlib modules
- Read and write CSV files for spreadsheet data
- Work with JSON data for structured information
- Handle file errors properly (FileNotFoundError, PermissionError)
- Work with binary files
- Build practical file-based applications

## 📂 Directory Structure

- **examples/** - Working code examples from the chapter
- **exercises/** - Practice exercises for you to complete
  - **solutions/** - Full solutions (try exercises first!)

## 🎯 What You'll Learn

Real programs need to save and load data. This chapter teaches you to work with files - reading input, saving output, and processing data in various formats. You'll learn to work with text files, CSV spreadsheets, and JSON data, making your programs able to persist information between runs.

## 📝 Examples

- **01-basic-file-reading.py** - Reading files the simple way
- **02-with-statement.py** - Using context managers (recommended!)
- **03-reading-line-by-line.py** - Processing files line by line
- **04-count-words-in-file.py** - Practical file reading example
- **05-write-mode.py** - Writing files (overwrites existing)
- **06-append-mode.py** - Appending to files
- **07-save-notes-with-timestamp.py** - Adding timestamps to logs
- **08-using-os-module.py** - File paths with os module
- **09-using-pathlib.py** - Modern file paths with pathlib
- **10-reading-csv.py** - Reading spreadsheet data
- **11-writing-csv.py** - Creating CSV files
- **12-contact-manager-csv.py** - Complete CSV application
- **13-reading-json.py** - Loading JSON data
- **14-writing-json.py** - Saving JSON data
- **15-settings-class-json.py** - Application settings with JSON
- **16-error-handling-files.py** - Handling file errors properly
- **17-binary-files.py** - Working with binary data
- **18-note-taking-app.py** - Complete note-taking application

## ✏️ Exercises

- **exercise-01.py** - Count lines, words, and characters in a file
- **exercise-02.py** - Copy a file to a new location
- **exercise-03.py** - Read a CSV of students and calculate class average
- **exercise-04.py** - Create an expense tracker with JSON
- **exercise-05.py** - Find and replace text in a file
- **exercise-06.py** - Analyze log files and count errors

## 🚀 How to Use

1. Read Chapter 7 in the book
2. Run the examples: `python3 examples/02-with-statement.py`
3. Try the exercises: `python3 exercises/exercise-01.py`
4. Check solutions when ready (note: some exercises may not have solution files)

## 💡 Tips

- Always use `with open()` - it automatically closes files even if errors occur
- Use "r" for reading, "w" for writing (overwrites), "a" for appending
- Remember to convert strings to int/float when reading numbers
- CSV module handles commas and quotes in data properly - use it!
- JSON is perfect for structured data but can't handle all Python types
- Use pathlib.Path for modern, cross-platform file path handling
- Test file operations with small test files first
- Always handle FileNotFoundError when reading files

---

**Previous**: [Chapter 6 - Working with Strings](../chapter-06/) | **Next**: [Chapter 8 - Error Handling](../chapter-08/)
