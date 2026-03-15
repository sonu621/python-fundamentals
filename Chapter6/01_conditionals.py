# Conditionals Operators in Python are used to perform comparisons between values. They return a Boolean value (True or False) based on the comparison.

# Comparison Operators
age = int(input("Enter your age: "))

if (age>=18):
    print("You are eligible to vote.")
    print("Enjoy your voting experience!")
else:
    print("You are not eligible to vote yet.")
    print("Please wait until your 18th birthday!")

# Other Comparison Operators Examples
weight = int(input("Enter weight of person 1: "))

if weight < 0:
    print("Invalid weight entered.")
elif weight > 68:
    print("Person is overweight.")
elif weight == 0:
    print("Weight cannot be zero.")
else:
    print("Person has a healthy weight.")

# Quick Quiz: Write a  program to print yes when the age entered by the user is greater than or equal to 18.
user_age  = int(input("Enter your age: "))

if user_age >= 18:
    print("Yes")
else:
    print("No")


