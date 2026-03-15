# -------- Global Variable -------------------

## A global variable is a variable that is defined outside any function and can be accessed anywhere in the program.

# global variable
num = 10

def function():
    global num
    num = 3 # local variable
    print(num)

print(num)
function()
