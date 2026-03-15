name = "Sonu"
print("Greetings", name, "How are you today?") # Output using commas: Greetings Sonu How are you today?

greeting = f"Greetings {name}, How are you today?"
print(greeting) # Output using f-string: Greetings Sonu, How are you today?

nameslice = name[0:3]
print("Sliced part of the name", nameslice) # Output: Sliced part of the name Son

pickedcharacter = name[2]
print("Picked character from the name:", pickedcharacter) # Output: Picked character from the name: n

title = "Gupta"
titleslice = title[0:4]
print("Sliced part of the title", titleslice) # Output: Sliced part of the title: Gupt

fullname_String = name + " " + title
print("Full name of this learner developer is:", fullname_String) # Output: Full name of this learner developer is: Sonu Gupta

print(name[-2: -1]) # Output of negative indexing: u

# Slicing With Skip Value
word = "Developer"
print(word[0:8:2]) # Output with skip value: Dvlpr

# String in built functions
value = "World"
print(len(value))
print(value.endswith("l")) # Output: False
print(value.endswith("d")) # Output: True
print(value.count("o")) # Output: 1
print(value.capitalize()) # Output: World
print(value.upper()) # Output: WORLD
print(value.lower()) # Output: world
print(value.replace("o", "a")) # Output: Warld
print(value.startswith("W")) # Output: True
print(value.startswith("w")) # Output: False

# Escape Sequences Characters
print("Hello\nWorld")
print("Greetings", name, "How are you \"today?\"")  # Output for the double quote in single string we can use like this using bacl-slash

