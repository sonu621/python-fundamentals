# ------------------- List Comprehension -------------------

# A list comprehension is a concise way to create a new list by applying an expression to each item in an existing iterable
# (like a list, tuple, or range), optionally including a condition.

## Note: It’s like a shortcut for a for loop that builds a list in one line.


mylist = [2, 4, 6, 8]

squarelist = [i * i for i in mylist]
print(squarelist)