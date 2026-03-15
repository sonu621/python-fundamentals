# -----------------Using try-except ----------------------

# Prevents your program from crashing

try:
    # Ask the user to enter a number
    num = int(input("Hey, please enter any number: "))
    
    # Print the number
    print("You entered:", num)

except ValueError:
    # This runs if the user enters something that is not a number
    print("Error: Please enter a valid number.")

print("Thank you!")