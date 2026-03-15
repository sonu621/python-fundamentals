# ------------------- Try with else Clause -----------------

## Somtimes we want to run a piece of code when try was successful.

try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid number")
    
else:
    print("I'm inside the else!")