'''try:
    # Ask the user to enter two numbers
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    # Check for division by zero
    if second_number == 0:
        raise ZeroDivisionError("You cannot divide by zero.")

    # Perform division
    result = first_number / second_number
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid whole numbers.")

except ZeroDivisionError as error:
    print("Error:", error)

print("Program finished.")'''


try:
    first_number = int(input("Enter the number: "))
    second_number = int(input("Enter the number: "))

    if second_number == 0:
        raise ZeroDivisionError("Python cannot divided by zero!")
    
    result = first_number / second_number
    print("Result:", result)
    
except ValueError:
    print("Please enter a valid nuber!")

except ZeroDivisionError as error:
    print("Error:", error)

print("Program End!")