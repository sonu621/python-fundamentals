# Easy way to write the code for the beginner and this is for the fixed variables
'''class Employee():
    name = "Sonu"
    salary = 120000
    language = "Python"

User = Employee()
print(User.name, User.language, User.salary)'''

# This is the intermidiate level and print own data

'''class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

User = Employee("Sonu", 150000, "Software Developer")
User1 = Employee("Antoine Elias", 300000, "Manager")

print(User.name, User.position, User.salary)
print(User1.name, User1.position, User1.salary)'''
    

# This is advance way practice to print own data in single print function no need to write multiple times code

'''class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def display_info(self):
        print(f"My name is {self.name} working as {self.position} and earns {self.salary}")

User = Employee("Sonu Gupta", 200000, "Software Engineer")
User1 = Employee("Antoine Elias", 400000, "Manaager")

User.display_info()
User1.display_info()'''

