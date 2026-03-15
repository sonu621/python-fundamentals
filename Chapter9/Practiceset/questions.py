# Question 1: Write a program to read text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.
'''file = open("poems.txt")
content = file.read()
if ("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinle is not present in the content")
file.close()'''

# Question 2: The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file
## 'Hi- score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever
### the game() function vreaks the Hi-score.

'''import random

def game():
    print("You are playing a game..")
    score = random.randint(1, 62)
    with open("hiscore.txt", "r") as file:
        hiscore = file.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

        print(f"Your score: {score}")
        print(f"Previous High Score: {hiscore}")

        if (score > hiscore):
            print("🎉 New High Score!")
            with open("hiscore.txt", 'w') as file:
                file.write(str(score))
        return score
game()'''

# Question 3: Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these
## files in a folder fr a 13 - years old.
'''import os
def generateTable(n):
    table = ""
    table = f"Multiplication Table of {n}\n"
    table += "-" * 25 + "\n"

    for i in range(1, 11):
        table += f"{n} * {i} = {n * i}\n"

    os.makedirs("tables", exist_ok=True)

    with open(f"tables/table_{n}.txt", "w") as file:
        file.write(table)
    
for i in range(2, 21):
    generateTable(i)
print("🎉 All tables generated beautifully!")'''

# Question 4: A file contains a word "Donkey" multiple times. You need to write a program which replace this
## word "*****" by updating the same file.

'''word = "Donkey"

with open("sample.txt", "r") as file:
    content = file.read()

contentNew = content.replace(word, "#####")

with open("sample.txt", "w") as file:
    file.write(contentNew)

print("✅ All variations of 'Donkey' replaced.")'''


# Question 5: Repeat program 4 for a list of such words to be censored.

'''import re

list = ["Bad", "Harmfull", "Bad touch"]

with open("sample.txt", "r") as file:
    content = file.read()

for word in list:
    pattern = r"\b" + re.escape(word) + r"\b"
    content = re.sub(pattern, "#" * len(word), content, flags=re.IGNORECASE)
    content = content.replace(word, "#" * len(word))

with open("sample.txt", "w") as file:
    file.write(content)

print("All bad words censored!")
'''

# Question 6: Write a program to mine a sample file and fnd out whether it contains 'python'.

'''with open("sample.txt", "r") as file:
    content = file.read().lower()

count = content.count("python")

if ("python" in content):
    print(f"Python is present in the 'sample.txt' file {count} times.")
else:
    print("Python is not present in the 'sample.txt' file!")'''

# Question 7: Write a program to find out the line numbr where python is present from question 6.


'''with open("sample.txt", "r") as file:
    lines = file.read().lower()

lineno = 1
count = lines.count("python")
for line in lines:
    if("python in line"):
        print(f"Yes python is present. Line no: {lineno} and count {count}")
        break
    else:
        ("Python is not present in the file")'''

# Question 8: Write a program to make a copy of file "sample.txt"

'''with open("file.txt", "r") as file:
    content = file.read()

with open("sample.txt", "w") as file:
    content = file.write(content)
print("Copy past all the content!")'''

# Question 9: Write a program to find out whether s file is identical & matches the content of another file.

'''with open("file.txt", "r") as file, open("file1.txt", "r") as file1:
    if file.read() == file1.read():
        print("Yes, this both file content is identical!")
    else:
        print("No, this both file content is not identical!")'''

# Question 10: Write a program to wipe out the content of a file using python.

'''with open("file1.txt", "w") as file:
    file.write("")
print("Wipe out the file!")'''

# Question 11: Write a program to rename a file to "renamed_by_python.txt."

'''import os

if os.path.exists("file1.txt"):
    os.rename("file1.txt", "renamed_by_python.txt")
    print("File renamed successfully!")
else:
    print("File does not exist!")'''

