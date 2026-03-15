import pyttsx3

engine = pyttsx3.init()
# engine.say("Hello! This is a test of pyttsx3 in VS Code.")
engine.runAndWait()

number = 2

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
number = 10

import pyttsx3
engine = pyttsx3.init()
name = input("Enter your name: ")
engine.say(f"Hello, {name}! Welcome to the text to speech program.")
print(f"Greeting has been spoken for {name}.")

num1 = 5
num2 = 6
operation = "+"

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
# and so on
print("The result is:", result)