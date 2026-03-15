# --------------------------- The Perfect Guess Project -------------------------------

# We are going to create a program that generates a random number and asks the user to guess it.
# If the player's guess is higher than the actual number, the program displays:

# "Lower number, please."

# Similarly, if the user's guess is lower than the actual number, the program displays:

# "Higher number, please."

# When the user guesses the correct number, the program displays the number of guesses the player used to reach the correct answer.
# Hint: Use the random module.
'''
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

user_guess = -1
guess_count = 0

while user_guess != secret_number:
    user_guess = int(input("Guess the number: "))
    guess_count += 1

    if user_guess > secret_number:
        print("Lower number please.")
    elif user_guess < secret_number:
        print("Higher number please.")

print(f"You guessed the number {secret_number} correctly in {guess_count} attempts!")
'''
'''
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

max_attempts = 5
attempts_used = 0

print(f"(Debug) The secret number is: {secret_number}")  # For testing only

print("Welcome to The Perfect Guess Game!")
print(f"You have {max_attempts} attempts to guess the number between 1 and 100.\n")

while attempts_used < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts_used += 1

    if guess > secret_number:
        print("Too high! Try a lower number.\n")
    elif guess < secret_number:
        print("Too low! Try a higher number.\n")
    else:
        print(f"\n🎉 Congratulations! You guessed it in {attempts_used} attempts.")
        break
else:
    # This runs if the loop finishes without a correct guess
    print("\n❌ Game Over!")
    print(f"The correct number was {secret_number}.")
'''

import random

secret_number = random.randint(1, 100)

max_attempt = 5
attempt_used = 0

print(f"(Debug) Your secret number is {secret_number}")
print("Welcom to the Perfect Guess Game!")
print(f"You have total {max_attempt} attempt to guess the number 1 to 100!")

while attempt_used < max_attempt:
    guess = int(input("Enter the guess number: "))
    attempt_used += 1

    if guess > secret_number:
        print("Too High! Enter lower number.")
    elif guess < secret_number:
        print("Too Low! Enter Higher number.")
    else:
        print(f"Congratulations! You guess the correct number {secret_number} in {attempt_used} attempt")
        break
else:
    print("Game Over!")
    print(f"You used the total {attempt_used}, secrect number is {secret_number}")