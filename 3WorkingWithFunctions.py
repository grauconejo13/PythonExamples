# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:24:29 2023

@author: vanes
"""

# 1.	Actual and formal arguments are important part of a program. The difference Between Actual and Formal Parameters is that the actual parameter is used to invoke the information while executing the program, but the formal parameters are declared while calling the function.
#Show the use of formal and actual arguments by taking x, y and z. Pass the values 55, 77 and 88 to print it on the screen.

def print_numbers(x, y, z):
    print("x:", x)
    print("y:", y)
    print("z:", z)

# Pass actual arguments 55, 77, 88 to the function
print_numbers(55, 77, 88)
print("\n")

#2.	Print the id = 77898, qualification = PhD and name = Grace, by using the keyword variable length argument (**variable) in python.

def print_info(id, name, **qualifications):
    print("ID:", id)
    print("Name:", name)
    for key, value in qualifications.items():
        print(key, "=", value)

# Pass variable length arguments to the function
print_info(id=77898, name="Grace", qualification="PhD")
print("\n")


#3.	Show the use of default arguments in python. The function shop has parameters as items and price. Let’s say the price of many items is $5 by default. In this case, we can set the price parameter to the default value of $5. Though, Price has a default value of 5. Still, if we provide the values at the time of calling then the default values will be overridden with the passed values.

#Create a function by name shop with the keywords item, amount. Assign the amounts to the corresponding items, say purse = $35, bag = $70.  Print the items pen, purse, bag and their amount.

def shop(item, amount, price=5):
    print("Item:", item)
    print("Amount:", amount)
    print("Price per item:", price)
    total_price = amount * price
    print("Total price:", total_price)

# Call the function with only required arguments
shop("pen", 4)

# Call the function with overridden default value
shop("purse", 1, 35)

# Call the function with both required and default arguments
shop("bag", 2, 70)






