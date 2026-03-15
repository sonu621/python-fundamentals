## With statement in Python

file = open("file.txt")
print(file.read())
file.close()

## The same can ve written using with statement like this:
with open("file.txt") as file:
    print(file.read())

## Note: Using with statement, dont have to explicitly close the file