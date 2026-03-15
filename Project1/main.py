# # Project 1: Snake, Water, Gun Game
# '''
# 1 for Snake
# -1 for water
# 0 for gun
# '''

import random

computer = random.choice([-1, 0, 1])
user_input = input("Enter your choise: ").lower()
database = {"snake": -1, "gun": 0, "water": 1}
reversDict = {-1: "Snake", 0: "Gun", 1: "Water"}
you = database[user_input]
print(f"You choose {reversDict[you]}\nComputer choose {reversDict[computer]}")
if computer == you:
    print("It's a Draw!")
else:
    if computer == -1 and you == 0:
        print("You win!")
    elif computer == -1 and you == 1:
        print("Computer win!")
    elif computer == 0 and you == -1:
        print("Computer win!")
    elif computer == 0 and you == 1:
        print("You win!")
    elif computer == 1 and you == -1:
        print("You win!")
    elif computer == 1 and you == 0:
        print("Computer win!")
    else:
        print("Somthing went wrong!")

'''import random

computer = random.choice([-1, 0, 1])
user_input = input("Enter your choice: ").lower()
database = {"snake" : 1, "gun" : -1, "water" : 0}
reverseDict = {1 : "Snake", -1 : "Gun", 0 : "Water"}
you = database[user_input]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if computer == you:
    print ("It's a Draw!")

else:
    if computer == -1 and you == 1:
        print("You Lose! 😢")
    elif computer == -1 and you == 0:
        print ("You Win! 🎉")
    elif computer == 0 and you == 1:
        print("You Win! 🎉")
    elif computer == 0 and you == -1:
        print("You Lose! 😢")
    elif computer == 1 and you == -1:
        print("You Lose! 😢")
    elif computer == 1 and you == 0:
        print("You Win! 🎉")
    else:
        print("Somthing went wring!")'''
