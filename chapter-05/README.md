# Chapter 5: Data Structures

## 📚 Learning Objectives

By the end of this chapter, you will be able to:
- Create and manipulate lists (ordered, changeable collections)
- Work with tuples (ordered, unchangeable collections)
- Use sets for unique collections and set operations
- Create and use dictionaries with key-value pairs
- Choose the right data structure for your needs
- Use list comprehensions for concise code
- Work with nested data structures

## 📂 Directory Structure

- **examples/** - Working code examples from the chapter
- **exercises/** - Practice exercises for you to complete
  - **solutions/** - Full solutions (try exercises first!)

## 🎯 What You'll Learn

Move beyond single values to working with collections of data. This chapter introduces Python's powerful built-in data structures: lists for ordered collections, tuples for immutable data, sets for unique items, and dictionaries for key-value pairs. You'll learn when and how to use each one effectively.

## 📝 Examples

- **01-list-operations.py** - Overview of list capabilities
- **02-creating-lists.py** - Different ways to create lists
- **03-accessing-elements.py** - Indexing and slicing lists
- **04-modifying-lists.py** - Adding, removing, and changing list items
- **05-common-list-operations.py** - Sort, reverse, count, and more
- **06-list-comprehension.py** - Concise list creation
- **07-looping-lists.py** - Different ways to iterate through lists
- **08-nested-lists.py** - Lists containing other lists
- **09-tuples-basic.py** - Creating and using tuples
- **10-tuple-operations.py** - Working with immutable sequences
- **11-list-tuple-conversion.py** - Converting between lists and tuples
- **12-sets-basic.py** - Creating and using sets
- **13-set-math-operations.py** - Union, intersection, difference
- **14-remove-duplicates.py** - Using sets to remove duplicates
- **15-dictionaries-basic.py** - Creating and using dictionaries
- **16-accessing-dict-values.py** - Getting values from dictionaries
- **17-modifying-dictionaries.py** - Adding, updating, removing items
- **18-dictionary-methods.py** - keys(), values(), items()
- **19-looping-dictionaries.py** - Iterating through dictionaries
- **20-nested-dictionaries.py** - Dictionaries containing other dictionaries
- **21-word-counter.py** - Practical dictionary application

## ✏️ Exercises

- **exercise-01.py** - Create and manipulate a list of favorite movies
- **exercise-02.py** - Filter even numbers from a list
- **exercise-03.py** - Find the second largest number in a list
- **exercise-04.py** - Create a dictionary representing a book
- **exercise-05.py** - Build a word length dictionary from a sentence
- **exercise-06.py** - Merge two dictionaries together
- **exercise-07.py** - Remove duplicates from a list while preserving order
- **exercise-08.py** - Create a phone book using a dictionary

## 🚀 How to Use

1. Read Chapter 5 in the book
2. Run the examples: `python3 examples/02-creating-lists.py`
3. Try the exercises: `python3 exercises/exercise-01.py`
4. Check solutions only after attempting: `python3 exercises/solutions/exercise-01-favorite-movies.py`

## 💡 Tips

- Lists are mutable (changeable), tuples are immutable (unchangeable)
- Use lists when you need to modify the collection
- Use tuples for data that shouldn't change (coordinates, RGB colors, etc.)
- Sets automatically remove duplicates - perfect for unique collections
- Dictionary keys must be unique and immutable (strings, numbers, tuples)
- List comprehensions are Pythonic: `[x*2 for x in range(10)]`
- Use .get() for dictionaries to avoid KeyError: `dict.get('key', default_value)`

---

**Previous**: [Chapter 4 - Functions & Modules](../chapter-04/) | **Next**: [Chapter 6 - Working with Strings](../chapter-06/)
