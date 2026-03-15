# Recursion - Recursion is a function whihck calls itself.
## If is used to directly use a mathematical formula as function.

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2*1
factorial(3) = 3*2*1
factorial(4) = 4*3*2*1
factorial(5) = 5*4*3*2*1

factorial(n) = n* n-1*....3*2*1
factorial(n) = n*factorial(n-1)
'''

## Best way to write the code
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter the number: "))
print(f"Factorial of {n} = {factorial(n)}")
