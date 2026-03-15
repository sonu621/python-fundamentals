# Class Method:-

## A class method is a method which is bound to the class and not the object of the class.
### @classmethod decorator is used to create a class method.

class Employee:
    name = "Sonu"

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name


print(Employee.name)   # Sonu
Employee.change_name("Sonu Gupta")
print(Employee.name)   # Sonu Gupta


