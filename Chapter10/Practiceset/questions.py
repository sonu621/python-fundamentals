# Question 1: Create a class "Programmer" for storing information of few programmers working at Microsoft.

'''class Programmer:
    company = "Microsoft" 
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def getinfo(self):
        print(f"{self.name} works as {self.position} at {Programmer.company}.")

employee = Programmer("Sonu Gupta", "SDEII")
employee1 = Programmer("Sanjiw Gupta", "SDEIII")

employee.getinfo()
employee1.getinfo()'''

# Question 2: Write a class "calculator" capable of finding square, cube and square root of a number.

'''import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The square is {self.number * self.number}")

    def cube(self):
        print(f"The cube is {self.number * self.number * self.number}")

    def square_root(self):
        print(f"The square root is {math.sqrt(self.number)}")

Result = Calculator(4)

Result.square()
Result.cube()
Result.square_root()'''

'''import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The square is {self.number ** 2}")

    def root(self):
        print(f"The root is {self.number ** 3}")
    
    def square_root(self):
        print(f"The square root is {math.sqrt(self.number)}")

result = Calculator(5)

result.square()
result.root()
result.square_root()'''

# Best way to write the code and best practice

'''import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The square is {self.number ** 2}")
    
    def cube(self):
        print(f"The cube is {self.number ** 3}")

    def square_root(self):
        print(f"The square root is {math.sqrt(self.number)}")
    
num = int(input("Please enter the number: "))

if num > 0:
    result = Calculator(num)
    result.square()
    result.cube()
    result.square_root()
else:
    print("Invalid number! Please enter the number greated than 0....")'''
        

# Question 3: Create a class with a class attribute a; create an object from it and set 'a' directly using object. a=o.
## Does this change the class attribute


'''class Demo:
    a = 10   # Class attribute

obj = Demo()

print("Before changing:")
print("Class attribute:", Demo.a)
print("Object attribute:", obj.a)


# Changing using object
obj.a = 0

print("\nAfter changing obj.a:")
print("Class attribute:", Demo.a)
print("Object attribute:", obj.a)'''

## Golden Rule
# Python checks attributes in this order:

# 1️⃣ Instance
# 2️⃣ Class

# If instance has it → use that
# If not → use class version

# Question 4. Add a static method in problem 2, to greet the user with hello.

'''import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The square of this number {self.number} is {self.number ** 2}")
    
    def cube(self):
        print(f"The cube of this number {self.number} is {self.number ** 3}")
    
    def square_root(self):
        print(f"The square root of this number {self.number} is {math.sqrt(self.number)}")
    
    @staticmethod
    def greet(name):
        print(f"Hey {name}, Welcom to the calculator world!")
    
user_name = input("Enter your name: ")
    
Calculator.greet(user_name)

num = int(input("Please enter the number: "))

if num > 0:
    result = Calculator(num)
    result.square()
    result.cube()
    result.square_root()
else:
    print("Invalid number! Please enter the number greater than 0....")'''

# Question 5: Write a class Train which has methods to book a ticket. Get status (no seats) and get fare information
## of train running under Indian Railways.

'''from random import randint

class Train:
    def __init__(self, train_number, total_seats):
        self.train_number = train_number
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_ticket(self, journey_start, journey_end):
        if self.available_seats > 0:
            self.available_seats -= 1
            print(f"✅ Ticket booked in Train No. {self.train_number} "
                  f"from {journey_start} to {journey_end}")
        else:
            print("❌ No seats available!")

    def get_status(self):
        print(f"🚆 Train No. {self.train_number} is running on time.")

    def get_fare(self, journey_start, journey_end):
        fare = randint(222, 5555)
        print(f"💰 Fare for Train No. {self.train_number} "
              f"from {journey_start} to {journey_end} is ₹{fare}")

    def get_available_seats(self):
        print(f"🪑 Available seats: {self.available_seats}")


# Creating an object
train = Train(12345, 1)

# Using methods
train.get_status()
train.get_available_seats()
train.book_ticket("Siwan", "Delhi")
train.get_fare("Siwan", "Delhi")'''


'''from random import randint

class Train():
    def __init__(self, train_number, total_seats):
        self.train_number = train_number
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_ticket(self, journey_start, journey_end):
        if self.available_seats > 0:
            self.available_seats -= 1
            print(f"✅ Ticket booked in Train number {self.train_number}"
                  f" from {journey_start} to {journey_end}")
        else:
            print("❌ No seats available!")

    def get_status(self):
        print(f"🚆 Train No. {self.train_number} is running on time")
    
    def get_fare(self):
        fare = randint(222, 5555)
        print(f"💰 Fare for Train No. {self.train_number} is ₹{fare}")
    
    def get_available_seats(self):
        print(f"🪑 Available seats: {self.available_seats}")

# Creating an object
train = Train(1234, 2)

# Using methods
train.get_status()
train.get_available_seats()
train.book_ticket("Siwan", "Delhi")
train.get_fare()'''

# from random import randint

# class Train:
#     def __init__(self, train_number, total_seats):
#         self.train_number = train_number
#         self.total_seats = total_seats
#         self.available_seats = total_seats

    
#     def book_ticket(self, journey_start, journey_end):
#         if self.available_seats > 0:
#             self.available_seats -= 1
#             print(f"Train No. {self.train_number} is booked from {journey_start} to {journey_end}!")
#         else:
#             print("❌ No seats available!")

#     def get_stauts(self):
#         print(f"Train No. {self.train_number} is running on time!")

#     def get_fare(self):
#         fare = randint(555, 9999)
#         print(f"Train fare is ₹ {fare}")

#     def get_available_seats(self):
#         print(f"🪑 Availble seats: {self.available_seats}")


# train = Train(12345, 0)

# train.book_ticket("Siwan", "Delhi")
# train.get_fare()
# train.book_ticket("Delhi", "Siwan")
# train.get_fare()
# train.get_available_seats()


# Question 6: Can you change the self-parameter inside a class to something else (say "Sonu"). try changing to "self" or "Sonu" and see the effects.

'''class Student:
    def __init__(Sonu, name):
        Sonu.name = name

    def show(Sonu):
        print("Name is:", Sonu.name)

s1 = Student("Sonu Gupta")
s1.show()'''
        
# Yes, we can change self to Sonu.
# It will still work.
# But using self is strongly recommended because it is standard practice and makes code readable.