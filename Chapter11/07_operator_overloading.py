# Operators Overloading Method:------

## Operators in Python can be overloaded using dunder methods.
## These methods are called when a given operators is used on the objects.
## Operators in Python can be overloaded using the following methods:

'''
p1 + p2   →  p1.__add__(p2)
p1 - p2   →  p1.__sub__(p2)
p1 * p2   →  p1.__mul__(p2)
p1 / p2   →  p1.__truediv__(p2)
p1 // p2  →  p1.__floordiv__(p2)
p1 % p2   →  p1.__mod__(p2)
p1 ** p2  →  p1.__pow__(p2)
'''

## Other dunder/magic methods in Python:
# str__() # Used to set what gets displayed upon calling str(obj)
# ___len___() # used to set what gets displayed upon calling. ___len__() or len(obj)

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

class Multiple:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value

num = 2
num1 = 5
print(num * num1)