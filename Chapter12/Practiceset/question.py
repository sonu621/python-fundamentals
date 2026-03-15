# Question 1: Write a program to open three files: 1.txt, 2.txt, and 3.txt. If any of these files are not present,
# a message should be printed without exiting the program, informing the user that the file does not exist.

'''
files = ["1.txt", "2.txt", "3.txt"]

for file_name in files:
    try:
        with open(file_name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"{file_name} does not exist.")

print("Thank You!")
'''

# Question 2: Write a program to print the third, fifth, and seventh elements from a list using the enumerate() function.

'''
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, item in enumerate(number_list):
    if index in(2, 4, 6):
        print(item)
'''

# Question 3: Write a list comprehension to create a list that contains the multiplication table of a number entered by the user.

# Correct way:-
'''
num = int(input("Enter any number: "))

table = [num * i for i in range (1, 11)]

print(table)
print("Thank You!")
'''


# Improvement (More Readable Output)
'''
num = int(input("Enter any number: "))

table = [num * i for i in range(1, 11)]

for i, value in enumerate(table, start=1):
    print(f"{num} x {i} = {value}")
'''

# Question 4: Write a program to display the result of a / b, where a and b are integers. If b = 0, handle
# the ZeroDivisionError and display "infinite" instead of crashing.

'''
try:
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    print(a / b)

except ZeroDivisionError:
    print("Infinite")

except ValueError:
    print("Please enter a valid number!")
'''

# Question 5: Write a program to store the multiplication tables generated in Problem 3 in a file named "tables.txt".

'''
num = int(input("Enter the number: "))

table = [num * i for i in range(1, 11)]

with open("tables.txt", "a") as file:
    file.write(str(table) + "\n")
'''

# In advance solution
'''
num = int(input("Enter the number: "))

with open("Tables.txt", "a") as file:
    file.write(f"The table of {num}\n")
    
    for i in range(1, 11):
        file.write(f"{num} x {i} = {num*i}\n")
    
    file.write("Thank you for input\n\n")
'''
