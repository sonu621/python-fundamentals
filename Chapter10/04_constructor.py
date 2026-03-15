#  ___int___() Constructor

## __int__() is a special method which is first run as soon the object is created.
## __int__() method is also know as constructor.

### It takes self - argument and can also take futher arguments.

# For example:

class Employee:
    def __init__(self, name):
        self.name = name

    def getInfo(self):
        print(f"My name is {self.name}")

User = Employee("Sonu Gupta")
User.getInfo()        