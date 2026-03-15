# Super() Method
## Super() method is used to access the method of a supper class in the derived class.

'''class Employee:
    def __init__(self, name):
        self.name = name

class Programming(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
    
class Designation(Programming):
    def __init__(self, name, language, designation):
        super().__init__(name, language)
        self.designation = designation

object = Designation("Sonu Gupta", "Python", "Manager")

print(f"Name is {object.name} skill have {object.language} hire as a {object.designation}")'''

