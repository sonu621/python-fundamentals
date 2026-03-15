# Property Decorators

'''class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def yearly_salary(self):
        return self.salary * 12

emp = Employee(10000)
print(emp.yearly_salary)'''

# Getter Setter Method

class Employee:
    def __init__(self, salary):
        self._salary = salary   # private variable

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative!")
        else:
            self._salary = value


emp = Employee(10000)

print(emp.salary)   # getter
emp.salary = 20000  # setter
print(emp.salary)

emp.salary = -5000  # validation
