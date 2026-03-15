'''
Function and Recursions

A function is a group of statements performing a specific task.

When a program gets bigger in size and its complexity grows, its gets difficult for a program to keep track on which
piece of code is doing what!

A function can be resued by the programmer in a given program any number of

There are two types of Function

1. Built in functions (Aleady present in python)
2. User defined functions (Defined by the user)

Examples of built functions includes len(), print(), range(), etc.

The func1() function we defined is an example of user defined function.
'''
# Function Definition
# def avg():
#     a = int(input("Please enter the A input: "))
#     b = int(input("Please enter the B input: "))
#     c= int(input("Please enter the C input: "))

#     average = (a + b + c)/3
#     print(average)
# avg() # Function call
# print("Thank You!")

# def fun1():
#     print("Hello World")
# fun1()

# Question - Great a user with good day
# def fun(name):
#     print("Good Day, " + name)

# name = input("Please enter the name: ")
# fun(name)


# def fun(name, ending):
#     print("Good Day, " + name)
#     print(ending)
#     return "Done!"

# name = input("Please enter your name: ")
# var = fun(name, "Thank You!")
# print(var)

# def calculate_average(a, b, c):
#     return(a + b + c)/3

# average1 = calculate_average(13, 35, 33)
# print(average1)

# average2 = calculate_average(45, 98, 28)
# print(average2)


# def avg(a, b, c):
#     return(a + b + c)/3

# a = float(input("Please enter the number: "))
# b = int(input("Please enter the number: "))
# c = float(input("Please enter the number: "))

# total = avg(a, b, c)
# print(total)

# Advance way baest practice
# def average(numbers):
#     return sum(numbers) / len(numbers)

# numbers = []

# for i in range(4):
#     num = float(input(f"Enter the number {i + 1}: "))
#     numbers.append(num)

# total_average = average(numbers)
# print("Average of the total number: ", total_average)

''' In Advance Practice
def greet(name, ending):
    print("Hello, " + name)
    print(ending)

for i in range(3):
   name = input("Please enter your name: ")
   greet(name, "Thank You!")
   '''

'''
Default Argument
def greet(name, ending="Done!"):
    print(f"Hello {name}")
    print(ending)

name = input("Enter your name: ")
greet(name,)
'''


def greet(name="Sonu", ending="Thank You!"):
    print(f"Hello, {name}")
    print(ending)

greet()

