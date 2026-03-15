# ------------------------ Virtual Environment -------------------

## A virtual environment is an isolated Python environment that allows you
## to install packages separately for different projects without affecting
## the system-wide Python installation.

## Installation ------

'pip install virtualenv'   # Install the virtualenv package


# ---------------- PIP Freeze Command ----------------

'pip freeze > requirements.txt'
# This command creates a file named "requirements.txt" in the same directory
# containing the list of all installed packages and their versions.

# Install packages from the file
'pip install -r requirements.txt'


# ---------------- Lambda Functions ----------------

# A lambda function is a small anonymous function created using the 'lambda' keyword.

# Syntax:
'lambda arguments: expression'

# Example:
'''
square = lambda x: x**2
print(square(5))  # Output: 25
'''

# Join Method -----------------

# Create a string from iterable objects.
'''
a = ["Sonu", "Rohan", "Sohan"]

final = "::".join(a)
print(final)
'''

# Formate Method (Strings)

# Formats the value inside the string into a desired output.
'''
a = "{} is a godd {}".format("Sonu", "boy")
print(a)

b = "{0} is a godd {1}".format("Sonu", "boy")
print(b)
'''

# ---------------- Map, Filter & Reduce ----------------

# map() applies a function to all the items in an input list.

'map(function, iterable)'

# Example: 
'''
num = [1, 2, 3, 4, 5,]

square = lambda x: x ** 2

square_list = map(square, num)
print(list(square_list))
'''

# filter() creates a list of items for which the function returns True.

'list(filter(function, iterable))'  # The function can be a lambda function

# Example:
'''
def even(n):
    if n % 2 == 0:
        return True
    return False

def odd(n):
    if n % 2 != 0:
        return True
    return False

numbers = [1, 2, 3, 4, 5, 6]

onlyEven = filter(even, numbers)
onlyOdd = filter(odd, numbers)

print(list(onlyEven))
print(list(onlyOdd))
'''

# reduce() applies a rolling computation to sequential pairs of elements.

'''from functools import reduce
val = reduce(function, list1)'''  # The function can be a lambda function

# Example: 

from functools import reduce

def add(a, b):
    return a + b

num = [2, 4, 34, 21]

square_list = map(lambda x: x**2, num)

print(reduce(add, num))
print(list(square_list))