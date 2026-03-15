user_age = int(input("Enter your age: "))

# Multiple if statements to check age ranges

# If statement no.1
if (user_age%2 ==0):
    print("Your age is an even number. ")
# End of the statement no.1 

# If statement no.2
if (user_age>=18):
    print("You are eligible to vote.")
elif(user_age<0):
    print("Invalid age entered.")
else:
    print("You are not eligible to vote.")
# End of the statement no.2

# There can be any numbers of elif statements after an if statement.
# Last else executed only if all the conditions inside elif fail.