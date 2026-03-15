# Question 1: Write a python program to display a user entred name followed by Good Afternoon using input() function.
# user_name = input("Please enter the user name: ")
# print(f"Good After Noon, {user_name}")
# print("Good After Noon:", user_name)

# Question 2: Write a program to fill in a letter template given below with name and date.
# letter_template = '''Dear <|Name|>, You'r DOB is <|Date|>'''

# user_name = input("Please enter your name: ")
# user_dob = "10-10-2000"
# print(letter_template.replace("<|Name|>", user_name).replace("<|Date|>", user_dob))

# Question 3: Write a program to detect double space in a string.
# string_with_double_space = "This  string with double  space."
# print(string_with_double_space.find(" "))

# Question 4: Replace the double space from the problem 3th single spaces.
# string_with_three_space = "Hey user, Welcome   back   to your POD!"
# print(string_with_three_space.replace("   ", " "))

# Question 5: Write a program to format the following letter using escape sequence characters.
# from datetime import datetime
# escape_letter = f"Dear {user},\n\tThis python course is nice. \nThanks!"
# current_tim = datetime.now()
# print(escape_letter)
user_name = ["Sonu Gupta", "Mr. Firass", "Pihu"]
escape_letter = f"Dear {user_name[2], "user"}, \n\tThis Python course is not"
print(escape_letter)

## --------------- From ChatGPT Questions ---------------- ##
# Question 2: Reverse a string
# def reverse_string(s):
#     return s[:: -1]

# print(reverse_string("Sonu"))

# Question 3: Check if a number is even or odd
# def is_even(n):
#     return n% 2 ==0

# print(is_even(10))
# print(is_even(7))

# Question 4: Find the largest number in a list
# def largest_number(lst):
#     largest = lst[0]
#     for num in lst:
#         if num > largest:
#             largest = num
#     return largest

# print(largest_number([10, 4, 25, 7]))        

# Question 5: Sum of all elements in a list
# def sum_list(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total
# print(sum_list([1, 2, 4, 6]))

# Question 6: Check a string is a palindrome
# def is_palindrom(s):
#     return s == s[::-1]

# print(is_palindrom("radar"))
# print(is_palindrom("hello"))

# Question 7: Remove duplicates from a list
# def remove_duplicates(lst):
#     return list(set(lst))

# print(remove_duplicates([1, 2, 3, 2, 4, 5, 6, 6, 0]))

# Question 8: Factorial of a number (iterative)
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial(5))

# Question 9: Generate a list of squares
# def squares_list(n):
#     return [i**2 for i in range(1, n + 1)]

# print(squares_list(6))

# Question 10: Find common elements in two lists
# def common_elements(list1, list2):
#     return [item for item in list1 if item in list2]

# print(common_elements([1,2,3,4], [2,4,5,6]))