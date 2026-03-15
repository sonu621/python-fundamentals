# Question 1: Write a program to store seven fruits in a list entered by the users.
# fruits = []
# for i in range(7):
#     fruits.append(input(f"Enter the name of fruits {i + 1}:"))
#     print("Total 7 fruits:", fruits)

# Question 2: Write a  program to accept marks of 6 students and display them in stored manner.
# marks = []

# for i in range(6):
#     mark = int(input(f"Enter marks of student {i+1}: "))
#     marks.append(mark)

# print("Marks of 6 students:", marks)

# Question 4: Check that a type conanot be changed in python.
# my_tuple = (1, 2, "Sonu", True)

# my_tuple[2] = "Sapna" # This will raise a typeerror because tuples are immutable

# Question 5: Write a program to sum a list with 4 numbers
# list = [12, 20, 40, 24]
# print("Sum of the list is:", sum(list))

# Question 6: Write a program to count the number of zeros in the following tuple:
tuple_list = (6, 0, 1, 0, 5, 0)
print("Numbers of zeros in the tuple is:", tuple_list.count(0)) # Output: 3 zeros
print("Index of first zero in the tuple is:", tuple_list.index(0))