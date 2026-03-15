# Loops in Python - Used to execute a block of code repeatedly until a creation condition is met.
# Types of Loops:
# 1. For Loop
# 2. While Loop

# While Loop Example:-
i = 1
while(i < 6):
    print(i)
    i += 1

'''
While Loop = The condition keeps executing until the condition is true
Output will be:
1
2
3
4
5
'''

# Quick Quiz: Write a program to print 1 to 7 using a while loop.
i = 0
while (i < 7):
    print(i)
    i += 1

# # Print a Name N Times (User Input)
name = input("Please enter your name: ")
times = int(input("How many times? "))

i = 0
while(i < times):
    print(name)
    i += 1


# Note: If the condition never become false, the loop keeps getting executed.

# Quick Quiz: Write a program to print the content of list using while loop.
userlist = ["Sonu", "Monu", "Sona", "Mona"]

i = 0
while(i < len(userlist)):
    print(userlist[i])
    i += 1

# For Loop Example:-
## A for loop is used to iterate through a sequence like list, tuple, or string [iterables]
for i in range(4):
    print(i)

# # For Loops with List
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)

# # For Loop with Tuples
tuples = (6, 231, 75, 122)
for i in tuples:
    print(i)

# # For Loop with strings
string = "Sonu"
for i in string:
    print(i)

# For Loop with Else:-
## An optional else can be used with a for loop if the code is to be executed when loops exhausts.
list = [1, 7, 27]

for item in list:
    print(item)
else:
    print("Done") # This is pronted when the loop exhausts!

# The Break Statement
## "Break" is used to come out of the loop when encountered. It instructs the program to exit the loop now.
for i in range(10):
    if (i == 5):
        break # Exit the loop rigth now
    print(i)

# The Continue Statement
## "Continue" is used to stop the current iteration of the loop and continue with the nect one. It instructs the Program to "skip this iteration".
for item in range(10):
    if (item == 5):
        continue # Skip this iteration
    print(item)

# Another example:-
for item in range(4):
    print("Printing")
    if item == 2: # If itesm is 2, the iteration is skipped
        continue
    print(item)

# Pass Statement:-
## Pass is a null statement in Python. It instructs to "do nothing".
list = [1, 7, 8]
for item in list:
    pass # Without pass, the program will thrwo an error