# Dictionary in Python is a collection of key-value pairs. Each key is unique and is used to store and retrieve values.
# Creating a dictionary
my_dict = {
    "name": "Sonu",
    "age": 25,
    "is_student": False,
    "courses": ["Math", "Science", "English"]
}
# Accessing values using keys
print(my_dict["name"]) # Output: Sonu
print([my_dict]) # Output: Entire dictionary
print(my_dict["age"]) # Output: 25
print(my_dict["courses"][1]) # Output: Science
print(my_dict.get("is_student")) # Output: False

# Adding a new key-value pair
my_dict["grade"] = "A"
print(my_dict["grade"])

# Modifying values
my_dict["age"] = 26
print(my_dict["age"]) # Output: 26

# Removing a key value pair
del my_dict["is_student"]

# Accessing the updated entire dictionary list
print([my_dict])

# Dictionary Methods
# Items method
print(my_dict.items()) # Output: dict_items([('name', 'Sonu'), ('age', 26), ('courses', ['Math', 'Science', 'English']), ('grade', 'A')])

#Keys method
print(my_dict.keys()) # Output:dict_keys(['name', 'age', 'courses', 'grade'])

# Values method
print(my_dict.values()) # Output: dict_keys(['name', 'age', 'courses', 'grade'])

# Update method
my_dict.update({"age": 25, "grade": "A+"})
print(my_dict) # Output: {'name': 'Sonu', 'age': 25, 'courses': ['Math', 'Science', 'English'], 'grade': 'A+'}

# Get method
print(my_dict.get("name")) # Output: Sonu
print(my_dict.get("address")) #Output: None(since address key does not exist)

# Pop method
removed_value = my_dict.pop("courses")
print(removed_value) # Output: ['Math', 'Science', 'English']

# Clear method
my_dict.clear()
print(my_dict) # Output: {}