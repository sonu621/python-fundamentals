# Question 1: Create a class (2-D vector) and use it to create another class representing a 3-D vector.

'''class TwoVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"2D Vector: ({self.x}, {self.y})")


class ThreeVector(TwoVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    def show(self):
        print(f"3D Vector: ({self.x}, {self.y}, {self.z})")


# 2D object
v2 = TwoVector(1, 2)
v2.show()

# 3D object
v3 = ThreeVector(3, 4, 5)
v3.show()'''

# Question 2: Creats a class "Pets" from a class "Animals" and futher create a class "Dog" from "Pets". Add a method "bark" to class "Dog"

'''
class Animals:
    def eat(self):
        print("Animal is eating")


class Pets(Animals):
    def friendly(self):
        print("Pet is friendly")


class Dog(Pets):
    def bark(self):
        print("Bow bow!")


dog = Dog()
dog.eat()
dog.friendly()
dog.bark()
'''

# Question 3: Create a class "Employee" and add salary and increment properties to it.
'''
class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment
    
    def apply_increment(self):
        self.salary +=  self.increment
    
# Creating Object
emp = Employee(12000, 500)
print("Initial Salary:", emp.salary)

emp.apply_increment()
print("Salary after increment:", emp.salary)
'''


# Question 4: Using question 3 write a method "salaryAfterIncrement" method witha @property decorator
##  with a setter which changes the value of increment based on the salary.
'''
class Employee:
    def __init__(self, salary, increment):
        self.salary = salary          # original salary
        self.increment = increment    # increment in %

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # change increment based on new final salary
        self.increment = ((new_salary - self.salary) / self.salary) * 100


# Example
emp = Employee(12000, 10)

print("Original Salary:", emp.salary)
print("Salary After Increment:", emp.salaryAfterIncrement)

# Now set new final salary
emp.salaryAfterIncrement = 14570

print("New Increment (%):", emp.increment)
print("Updated Salary After Increment:", emp.salaryAfterIncrement)''' 

# Question 5: Write a "Complex" to represent complex numbers, along with overloaded operators "+" and "*"
## which adds and multiple them.

'''
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overload + operator
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # Overload * operator
    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real_part, imag_part)

    # Display complex number
    def __str__(self):
        return f"{self.real}real + {self.imag}imag"


# Example
c1 = Complex(2, 3)
c2 = Complex(4, 5)

print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)
'''

# Question 6: Write a class Vector representing a vector of n dimensions. Overload the + and * operators
## which calculates the sum and the dot(.) product of them.

'''
class Vector:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    
    def __add__(self, other):
        return Vector(
            self.v1 + other.v1,
            self.v2 + other.v2,
            self.v3 + other.v3
        )
    
    def __mul__(self, other):
        # Dot product
        return (
            self.v1 * other.v1 +
            self.v2 * other.v2 +
            self.v3 * other.v3
        )

    def __str__(self):
        return f"({self.v1}, {self.v2}, {self.v3})"


V1 = Vector(1, 2, 3)
V2 = Vector(4, 5, 6)
V3 = Vector(7, 8, 9)

print(f"Sum: {V1 + V2 + V3}")
print(f"V1 · V2 = {V1 * V2}")
'''

# Question 8: Write a __str__() method to print the vector as follows:
## 7i + 8j + 10k
### Asume vector of dimension 3 for this problem.

'''
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


v = Vector(7, 8, 10)
print(v)
'''

# Question 9: Override the __len__() method on vector of problem 5 to display the dimension of the vector.

'''
class Vector:
    def __init__(self, values):
        self.values = values   # Store components in a list

    def __len__(self):
        return len(self.values)   # Dimension of vector


# Example
v1 = Vector([1, 2, 3])


print("Dimension:", len(v1))
'''
