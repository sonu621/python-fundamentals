'''Question 1: Write a program to print multiplication table of a given number using for loop.
number = int(input("Please enter any number for the table: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")'''

''' Question 2: Write a program to greet all the person names stored in a 'user_list' and which starts with S.
user_list = ["Sonu", "Mona", "Sona", "Pihu"]

for name in user_list:
    if(name.startswith("S")):
        print(f"Hey {name}, Welcome back to the team!")

Another advance example 1:-
user_list = ["Sonu", "Firass", "Reda", "Antoine"]

for name in user_list:
    if(name.startswith("S")):
        print(f"Hey {name}, Welcome to the PMV Team!")
    elif(name.startswith(("F", "A"))):
        print(f"Dear {name}, Welcome to the PMV Department!")
    else:
        print(f"Hello {name} Sir, How are you!")

# Advance example 2:-
user_list = ['Sonu', 'Firass', 'Reda', 'Antoine']
other_users = []

for name in user_list:
    if (name == "Sonu"):
        print(f"Hey {name}, How are you?")
    else:
        other_users.append(name)
print(f"Hey Boss, {", ".join(other_users)}")'''

'''Question 3: Attempt problem 1 using while loop.
number = int(input("Please enter any number"))

i  = 1
while (i < 11):
    print(f"{number} * {i} = {number * i}")
    i += 1
'''

'''Question 4: Write a program to find whether a given number is prime or not.
number = int(input("Please enter any number: "))

if number <= 1:
    print("Number is not prime:", number)
else:
    for i in range(2, number):
        if number % i == 0:
            print("Number is not prime:", number)
            break
    else:
        print("Number is prime:", number)

Another example in advance way
number = int(input("Please enter any number "))

if number <= 1:
    print(f"{number} is not a prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
        else:
            print(f"{number} is a prime number")
'''

'''Question 5: Write a program to find the sum of first n nutural numbers using while loop.
n = int(input("Please enter any number: "))

i = 1
sum = 0
while(i <= n):
    sum += i
    i += 1
print(sum)
'''

# Question 6: Write a program to calculate the factorial of given number using for loop.
# n = int(input("Please enter any number: "))

# factorial = 1
# for i in range(1, n + 1):
#     factorial = factorial * i
# print(f"The factorial of {n} = {factorial}")

'''
Question 7: Write a program to print the following star pattern.
  *
 ***
***** for n = 3


n = int(input("Please enter the number: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")

# In Advance
n = int(input("Please enter the number: "))

for i in range(1, n + 1):
    print(" " * (n -i), end="")
    print(f"{n}" * (2 * i - 1), end="")
    print("")
'''

''' Question 8: Write a program to print the following star pattern:
*
**
***** for n = 3


n = int(input("Please enter the number: "))
for i in range(1, n + 1):
    print("*" * i, end="")
    print("")
'''

'''
Question 9: Write a program to print the following star pattern.
***
* * for n = 3
***

n = int(input("Please enter the number: "))

for i in range(1, n + 1):
    if(i==1 or i==n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    print("")
'''

'''
Question 10: Write a program to print multiplication table of n using for loops in reversed order.
'''
# n = int(input("Please enter the number: "))

# for i in range(1, 11):
#     print(f"{n} * {11 - i} = {n *(11 - i)}")

