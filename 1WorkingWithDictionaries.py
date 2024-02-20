# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 20:22:56 2023

@author: vanes
"""

# a.The solution to convert the given values into a dictionary and print the result using the update() method
courses = {}
courses.update({'COMP100': 'PROGRAMMING 1'})
courses.update({'COMP228': 'JAVA PROGRAMMING'})
courses.update({'COMP237': 'INTRO. TO AI'})
courses.update({'COMP246': 'SOFTWARE SYSTEMS DESIGN'})
courses.update({'COMP257': 'UNSUPERVISED LEARNING'})
courses.update({'COMP258': 'NEURAL NETWORKS'})
courses.update({'COMP387': 'IT SOLUTIONS'})
print(f"{courses}\n")


# b.Check if the value 'NEURAL NETWORKS' exists in the dictionary
if 'NEURAL NETWORKS' in courses.values():
    print("The value 'NEURAL NETWORKS' exists in the dictionary.\n")
else:
    print("The value 'NEURAL NETWORKS' does not exist in the dictionary.\n")


# c.Retrieve the value associated with key 'COMP237' using get() method
course_name = courses.get('COMP237')
print(f"{course_name}\n")

# d. Delete the keys 'COMP387' and 'COMP246' from the dictionary using del keyword
del courses['COMP387']
del courses['COMP246']
print(f"{courses}\n")

# e.Sort the dictionary by values in ascending order by using the sorted() function with the items() method
sorted_courses = dict(sorted(courses.items(), key=lambda item: item[1]))
print(sorted_courses)
