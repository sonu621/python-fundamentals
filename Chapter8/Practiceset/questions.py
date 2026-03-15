# Question 1: Write a program using function to find the greatest of three numbers

'''
Best way to write a code:- 
def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and a > c:
        return b
    else:
        return c

a = int(input("Enter the a number: "))
b = int(input("Enter the b number: "))
c = int(input("Enter the c number: "))
print(greatest(a, b, c))'''

'''
Advance Practice: -
def greates (a, b, c):
    return max(a, b, c)

a = int(input("Enter A = "))
b = int(input("Enter B = "))
c = int(input("Enter C = "))
print("Greatest number", greates(a, b, c))

Pro leverl Practice:
def greatest(numbers):
    if not numbers:
        return "Not number entred"
    return max(numbers)

numbers = []
n = int(input("Enter how many numbres: "))

for i in range(n):
    num = int(input(f"Enter the number {i + 1}: "))
    numbers.append(num)

print("Greatest number is: ", greatest(numbers))
'''

# Question 2: Write a python program using function to convert Celsius to Fahrenheit.

'''
def celsius_to_fahrenheit(celsius):
    return 5 * (celsius - 32) / 9

celsius = float(input("Enter the numberes in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)
print(f"Temperature in Celsius: {round(fahrenheit, 2)} °C" )'''

# Question 3: How do you prevent a python print() function to print a new line at the end.

'''print("Hello,", end=" ")
print("world!")'''

# Question 4: Write a recursive function to calculate the sum of the first n natural numbres.

'''def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

n = int(input("Enter the number: "))
total_sum = sum_natural(n)
print(f"The first number n {n} of natural: {total_sum}")'''

# Question 5: Write a python function to print first n lines of the following pattern:
'''
***
**   -for n = 3
*
'''

'''def pattern(n):
    for i in range(n, 0, -1):
        print("*"* i)

n = int(input("Enter the number: "))
pattern(n)'''

# Question 6: Write a python function which converts inches to cms.

'''def inches_to_cms(inches):
    return inches * 2.54

inches = float(input("Enter the lenght in inches: "))
cms = inches_to_cms(inches)
print(f"{inches} inches is equal to {round(cms, 2)}cms")'''

# Question 7: Write a python function to remove a given word form a list as strip it at the same time.

'''def remove_and_strip(words, word_to_remove):
    new_list = []
    for word in words:
        stripped_word = word.strip()
        if stripped_word != word_to_remove:
            new_list.append(stripped_word)
    return new_list


words = [" apple ", "banana ", " mango", "banana", "  orange  "]
result = remove_and_strip(words, "banana")

print(result)'''


# Question 8: Write a python function to print multiplication table pf given number.
'''def multiply(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

n = int(input("Enter the number: "))

multiply(n)'''
