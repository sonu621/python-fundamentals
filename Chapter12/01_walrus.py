# Newly Added Features In Python

## Following are some of the newly added features in Python programming language

### --------------------- Walrus Operator --------------------------------

# The Walrus Operator (:=) was introduced in Python 3.8.
# Its official name is the assignment expression operator.

# It allows you to assign a value to a variable as part of an expression.

# Before Python 3.8, you had to assign a variable on one line and then use it on another.

# Without walrus operator:
'''data = input("Enter something: ")
if data:
    print("You entered:", data)'''

# Using walrus operator, we can combine both step
'''if (data := input("Enter something: ")):
    print("You entered:", data)'''


# ------------------ Advance Types Hints ----------------------
# In modern Python (especially 3.9+), advanced types help you write clearer, safer, and more maintainable code using type hints.

# They are mainly provided by the built-in typing module.

# ---Typing module: --
'''list[int]
tuple[int, str]
set[str]
dict[str, int]'''

# ---- Union Types ----
'''int | float
Union[int, float]   # older style'''


# ----------------- Match Case in Python --------------------

# match-case was introduced in Python 3.10.
# It is used for pattern matching (similar to switch-case in other languages, but more powerful).

# For example:-
'''def check_status(status):
    match status:
        case "active":
            return "User is active"
        case "inactive":
            return "User is inactive"
        case _:
            return "Unknown status"

print(check_status("active"))'''


'''def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
          return  "Unknow Status"

print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(5001))'''


dict1 = {'a' : 1, 'b' : 2}
dict2 = {'c' : 3, 'd' : 4}

merged = dict1 | dict2

print(merged)