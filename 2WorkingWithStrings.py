# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 22:28:51 2023

@author: vanes
"""

#1.	Apply the positive and negative indexing to the string named as course. Print and show. Course = "Python"

course = "Python"
print(course[0])    # Positive indexing: first character
print(course[-1])   # Negative indexing: last character
print("------------------------------------------------")

#2.	Print the course name, character by character using for loop

course = "Python"
for c in course:
    print(c)
print("------------------------------------------------")

#3.	A string having immutable nature. Once we create a string object then we cannot change or modify the existing object. Show that by using the above course by change P to R

# course = "Python"
# course[0] = "R"
# print("------------------------------------------------")


#4.	Make use of the methods upper (), lower (), swapcase (), title (), capitalize () to change the cases of the given string in Python.  String = “centennial college courses”

string = "centennial college courses"

# Convert all characters to upper case
print(string.upper())

# Convert all characters to lower case
print(string.lower())

# Swap the case of characters
print(string.swapcase())

# Convert the first letter of each word to upper case
print(string.title())

# Convert the first letter to upper case
print(string.capitalize())
print("------------------------------------------------")

#5.	Give your own examples to perform two mathematical operators (+ and *) on a string.

# Example of using + operator on strings
string1 = "Hello"
string2 = "Kitty"
string3 = string1 + " " + string2
print(string3)

# Example of using * operator on strings
string4 = "Excalibur"
string5 = string4 * 3
print(string5)
