# -------------------- Try With Finally --------------------

# The finally block always runs, whether:

# An exception occurs 
# No exception occurs
# It is commonly used for:
# Closing files
# Releasing resources
# Cleaning up operations

'''
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Please enter a valid number")

finally:
    print("This will always execute")
'''


try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Closing program")
