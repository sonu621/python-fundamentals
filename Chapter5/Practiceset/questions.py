# Questions 1: Write a program to create a dictionary of hindi words with values as their English translations.Provide user with an option to look it up!
hindi_english_dict = {
    "namaste": "hello",
    "dost": "friend",
    "paani": "water",
    "billi": "cat"
}

word = input("Enter a Hindi word to translate: ").split()[0].lower()
print("The English translation is:", hindi_english_dict.get(word, "Word not found in dictionary."))

# Question 2: Write a program to input eight numbers from the user and display all the unique number (once).
numbers = []
for i in range(8):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    unique_numbers = set(numbers)
    print("Unique numbers so far:", unique_numbers)

# Question 3: Can we have a set with 18(int) and "18" (str) as a value in it?
my_set = {18, "18"}
print("Set with 18 and '18':", my_set) # Output: Set with 18 and '18': {18, '18'}, Yes we can have both as they different data types.

# Question 4: What will be the length of the following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('10')
print("Length of the set s is:", len(s)) # Output: Length of the set s is: 2, because 20 and 20.0 are considered equal in Python sets.


# Question 5: s = {} What is the type of 's' ?
s = {}
print("Type of s is:", type(s)) # Output: Type of s is: <class 'dict'>, because {} creates an empty dictionary, not a set.


# Question 6: Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that names are unique.
favorite_languages = {}
for i in range(4):
    name = input("Enter your name: ").strip()
    language= input("Enter your favorite programming language: ").strip()
    favorite_languages[name] = language
    print("Current favorite language dictionary:", favorite_languages)

# Question 7: If the names of 2 friend are same, what will happen to the program in problem 6?
favorite_languages = {
    "Alice": "Python",
    "Bob": "Java",
    "Alice": "C++" # Duplicate key
}

print("Favorite languages dictionary with duplicate names:", favorite_languages) # Output: Favorite languages dictionary with duplicate names: {'Alice': 'C++', 'Bob': 'Java'}, Because dictionary keys must be unique, the second entry for the name will be overwrite.

# Question 8: If language of two friends are same, what will happen to the program in problem 6?
favorite_languages = {
    "Alice": "Python",
    "Bob": "Python",
    "Sonu": "Java",
    "Monu": "C++"
}
print("Favorite languages dictionary with same languages:", favorite_languages) # Output: Favorite languages dictionary with same languages: {'Alice': 'Python', 'Bob': 'Python', 'Sonu': 'Java', 'Monu': 'C++'}, Because dictionary values can be duplicate, no issue.

# Question 9: Can you change the values inside a list which is contained in set my_set?
my_set = {1, 2, (3, 4), "Hello", True}
print("Original set:", my_set)

# Nothing will change as sets cannot contain mutable elements like lists.