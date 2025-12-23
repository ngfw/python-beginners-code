#!/usr/bin/env python3
"""
Chapter 5: Data Structures
Exercise 5.1: Create a list of your five favorite movies. Add one more, remove one, and print the final list.
"""

movies = ["Inception", "The Matrix", "Interstellar", "The Shawshank Redemption", "Pulp Fiction"]
print("Original movies:", movies)

movies.append("The Dark Knight")
print("After adding:", movies)

movies.remove("The Matrix")
print("Final list:", movies)
