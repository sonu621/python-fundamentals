# Note: Instance attributes take preference over class attribute during assigment & retrieval.

## When looking up for User.name attribute it check for the following:
### 1) Is attribute present in object?
### 2) Is attribute present in class?

class Employee:
    languange = "Python"

User = Employee()
User.languange = "Java"

print(User.languange)