# Question 1: Create two virtual environments. Install a few packages in the first environment.
# How can you create a similar environment in the second one?

'''
# Create first virtual environment
python -m venv env1

# Activate first environment (PowerShell)
.\env1\Scripts\Activate.ps1

# Install some packages
pip install pandas numpy matplotlib

# Save installed packages
pip freeze > requirements.txt

# Deactivate first environment
deactivate


# Create second virtual environment
python -m venv env2

# Activate second environment
.\env2\Scripts\Activate.ps1

# Install the same packages in the second environment
pip install -r requirements.txt
'''

# Question 2: Write a Python program to input the name, marks, and phone number of a student 
# and display the following message using the format() function:

'The name of the student is Sonu, his marks are 72 and phone number is 7079533746'

'''
user_name = input("Enter the user name: ")
user_marks = int(input("Enter the user makrs: "))
user_phone = int(input("Enter the user phone number: "))

result = "The name of the student is {}, his marks are {} and phone number is {}".format(user_name, user_marks, user_phone)
print(f"Result: {result}")
'''

# Question 3: A list contains the multiplication table of 7. 
# Write a Python program to convert the elements of the list into a vertical string of the same numbers.

'''
num = 7

table = [str(num * i) for i in range(1, 11)]

result = "\n".join(table)

print(result)
'''

# Question 4: Write a Python program to filter the numbers in a list that are divisible by 5.

'''
def divisible_by_5(n):
    if n % 5 == 0:
        return True
    return False

numbers = [50505, 45609235, 59853, 43942, 4753594, 505050]

divisible_filter = list(filter(divisible_by_5, numbers))

print(divisible_filter)
'''

# Question 5: Write a Python program to find the maximum number in a list using the reduce() function.

'''
from functools import reduce

numbers_list = [45, 78, 23, 89, 12, 67, 34]

def greater(a, b):
    if a > b:
        return a
    else:
        return b

maximum = reduce(greater, numbers_list)

print("Maximum number:", maximum)
'''

# Question 6: Run the pip freeze command for the system interpreter. Save the output and use
# it to create a similar virtual environment.

'''
# Step 1: Get the list of installed packages from the system interpreter
pip freeze > requirements.txt

# Step 2: Create a virtual environment
python -m venv env

# Step 3: Activate the virtual environment (PowerShell)
.\env\Scripts\Activate.ps1

# Step 4: Install the same packages in the virtual environment
pip install -r requirements.txt
'''

# Question 7: Explore the "Flask" module and create a web server using Flask and Python.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()