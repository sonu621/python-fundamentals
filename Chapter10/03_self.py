# Self parameter:---
### Self refers to the instance of the class. It automaticaly passed with a function call from an object.

class Employee:
    name = "Sonu"
    language = "Python"
    salary = 150000

    @staticmethod # Its means we don't need any object and properties from this function that's why I mark this static method.
    def greet():
        print("Good Morning!")

    def getinfo(self):
        print(f"My name is {self.name} know the language {self.language} and earning {self.salary}")

User = Employee()
User.language = "JavaScript"

User.greet()
User.getinfo()