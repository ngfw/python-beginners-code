# Chapter 6: Working with Strings

## 📚 Learning Objectives

By the end of this chapter, you will be able to:
- Use essential string methods (upper, lower, strip, replace, split, join)
- Format strings elegantly with f-strings, .format(), and %
- Work with multi-line strings
- Find and count substrings
- Validate string content (isalpha, isdigit, etc.)
- Parse and transform text effectively
- Perform common string operations for real-world tasks

## 📂 Directory Structure

- **examples/** - Working code examples from the chapter
- **exercises/** - Practice exercises for you to complete
  - **solutions/** - Full solutions (try exercises first!)

## 🎯 What You'll Learn

Strings are everywhere in programming. This chapter teaches you powerful techniques for manipulating text, from simple case conversions to complex parsing and validation. You'll master Python's string methods and learn multiple ways to format output professionally.

## 📝 Examples

- **01-string-basics.py** - String fundamentals review
- **02-string-sequence.py** - Accessing individual characters
- **03-string-immutability.py** - Why strings can't be changed in place
- **04-case-conversion.py** - upper(), lower(), capitalize(), title()
- **05-strip-whitespace.py** - Cleaning up strings
- **06-find-and-replace.py** - Finding and replacing substrings
- **07-count-occurrences.py** - Counting how many times text appears
- **08-split-and-join.py** - Converting between strings and lists
- **09-check-string-content.py** - isalpha(), isdigit(), isalnum()
- **10-old-style-formatting.py** - Using % formatting
- **11-format-method.py** - Using .format() method
- **12-f-strings.py** - Modern f-string formatting (recommended!)
- **13-advanced-formatting.py** - Padding, alignment, number formatting
- **14-multi-line-strings.py** - Working with multi-line text
- **15-string-concatenation.py** - Joining strings efficiently
- **16-validate-email.py** - Simple email validation
- **17-title-case-names.py** - Formatting names properly
- **18-extract-domain.py** - Parsing URLs
- **19-count-words.py** - Counting words in text
- **20-reverse-string.py** - Reversing text
- **21-palindrome-checker.py** - Checking for palindromes
- **22-censor-text.py** - Censoring inappropriate words
- **23-string-encoding.py** - Converting strings to bytes
- **24-raw-strings.py** - Using raw strings for special characters

## ✏️ Exercises

- **exercise-01.py** - Count vowels and consonants in a string
- **exercise-02.py** - Convert text to snake_case format
- **exercise-03.py** - Capitalize the first letter of each sentence
- **exercise-04.py** - Validate username format (alphanumeric, starts with letter)
- **exercise-05.py** - Remove all digits from a string
- **exercise-06.py** - Find the longest word in a sentence
- **exercise-07.py** - Check if two strings are anagrams
- **exercise-08.py** - Implement Caesar cipher encryption

## 🚀 How to Use

1. Read Chapter 6 in the book
2. Run the examples: `python3 examples/04-case-conversion.py`
3. Try the exercises: `python3 exercises/exercise-01.py`
4. Check solutions only after attempting: `python3 exercises/solutions/exercise-01-count-vowels-consonants.py`

## 💡 Tips

- Strings are immutable - methods return new strings, they don't modify the original
- F-strings are the modern, preferred way to format strings in Python 3.6+
- Use .strip() to clean user input before processing
- .split() and .join() are inverses of each other
- String methods are case-sensitive: "Hello" != "hello"
- Use raw strings (r"...") for regex patterns and Windows file paths
- .startswith() and .endswith() are better than slicing for checking prefixes/suffixes

---

**Previous**: [Chapter 5 - Data Structures](../chapter-05/) | **Next**: [Chapter 7 - File I/O](../chapter-07/)
