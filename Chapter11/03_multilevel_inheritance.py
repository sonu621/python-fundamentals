# Multilavel Inheritance

## For example: Grandfather → Father → Son

# Now imagine:
# Grandfather has land
# Father inherits land
# Son also inherits land
# This is multilevel inheritance.

## Easy way to understand: ----
'''class Employee:
    name = "Sonu Gupta"

class Programming(Employee):
    language = "Python"

class Designation(Programming):
    designation = "Manger"

final_output = Designation()

print(f"Name is {final_output.name} skill in {final_output.language} working as a {final_output.designation}!")'''



## Best practice way:----
'''class Employee:
    def __init__(self, name):
        self.name = name


class Programmer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language


class Manager(Programmer):
    def __init__(self, name, language, team):
        super().__init__(name, language)
        self.team = team


# Object of Manager
m = Manager("Rahul", "Python", 5)

print(f"Manager Name: {m.name}, Programming Language: {m.language}, Team Size: {m.team}")'''


