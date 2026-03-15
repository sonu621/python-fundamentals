# Multiple inheritance

'''class Employee:
    company = "WebEngage"
    def show_employee(self):
        print(f"The name is the company is {self.company}")
    
class Coder:
    language = "Python"
    def show_language(self):
        print(f"He know the {self.language} programming.")

class Salary(Employee, Coder):
    salary = 12000
    def show_salary(self):
        print(f"This employee working in this {self.company} and he know {self.language} programming and salary is {self.salary}")


employee = Employee()
coder = Coder()
salary = Salary()

salary.show_salary()'''


# Best Practice way:- 

'''class Employee:
    def __init__(self, company):
        self.company = company


class Coder:
    def __init__(self, language):
        self.language = language


class Salary(Employee, Coder):
    def __init__(self, company, language, salary):
        Employee.__init__(self, company)
        Coder.__init__(self, language)
        self.salary = salary

    def show_salary(self):
        print(f"This employee works at {self.company}, knows {self.language}, and earns {self.salary}")


emp = Salary("WebEngage", "Python", 12000)
emp.show_salary()'''

