# Question 1: Write a program to find the greatest of four numbers entered by the user.
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))
num4 = int(input("Enter the num4: "))

if (num1 >= num2 and num1 >= num3 and num1 >= num4):
    print("The greatest number is num1: ", num1)
elif(num2 >= num1 and num2 >= num3 and num2 >= num4):
    print("The greatest number is num2: ", num2)
elif(num3 >= num1 and num3 >= num2 and num3 >= num4):
    print("The greatest number is num3: ", num3)
else:
    print("The greatest number is num4: ", num4)

# Question 2: Write a program to find out whether a student has passed or failed if it requires a total of 40%
## and at least 33% in each subject to pass. Assum 3 subjects to pass. Assume 3 subject and take marks as an input from the user.
maths = int(input("Enter the marks of maths: "))
english = int(input("Enter the marks of english: "))
coding = int(input("Enter the marks of coding: "))

# Checking the total percentage of the coding
total_percentage = (maths + english + coding) / 3

if (total_percentage >= 40 and maths >= 33 and english >= 33 and coding >= 33):
    print("Student is passed by: ", total_percentage)
else:
    print("Student is failed by: ", total_percentage)

# Question 3: A spam comment is defined as a text containing following keywords:
# "Make a lot money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
input1 = "Make a lot money"
input2 = "buy now"
input3 = "subscribe this"
input4 = "click this"

message = input("Enter your message: ")

if ((input1 in message) or (input2 in message) or (input3 in message) or (input4 in message)):
    print("This is a spam message: ", message)
else:
    print("This is not a spam message: ", message)

# Question 4: Write a program to find whethere a given username conatins less than 10 characters or not.
user_name = input("Please enter the username: ")

if len(user_name) < 10:
    print("The username contains less than 10 characters:", user_name)
else:
    print("The username contains 10 or more characters:", user_name)


# Question 5: Write a program which finds out whether a given name is present in a list or not.
user_list = ["Sonu", "Firass", "Reda", "Antoine"]

user_name = input("Please enter the user name: ")

if (user_name in user_list):
    print("Give the username in the list ", user_list)
else:
    print("Given the user name not in the list ", user_list)

# Question 6. Write a program to calculate the grade of student from his marks from the following scheme:
## 90 - 100 => Ex, 80 - 90 => A, 70 - 80 => B, 60 -70 => C, 50 -60 => Pass and <50 => Fail
marks = int(input("Please enter your marks: "))

if(marks >= 90 and marks <= 100):
    grade= "Ex"
elif(marks >= 80 and marks < 90):
    grade = "A"
elif(marks >= 70 and marks < 80):
    grade = "B"
elif(marks >= 60 and marks < 70):
    grade = "C"
elif(marks >= 50 and marks < 60):
    grade = "Pass"
else:
    grade = "F"

print("According to the student's marks, the grade is: ", grade)

# Question 7. Write a program to find out whether a given post is talking about "Sonu" or not.
post = "Hey I'm Sonu, I want to share my some thoughts related about this Python lesson"

name = input("Enter a name to search: ").lower()

if name in post.lower():
    print("This post is talking about name: ", name)
else:
    print("This post is not talking about name: ", name)

