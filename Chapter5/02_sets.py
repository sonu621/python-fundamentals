# Sets in Python
# Set is a collection of non-repetitive elements which is unordered and unindexed.

# Creating a set
my_set = {"Apple", "Cherry", 1, 2, 3.5, True}
print("My set is:", my_set) # Output: Print all the data in the set

# Empty set
empty_Set = set() # Note: {} creates an empty dictionary, not a set
print("Empty set:", empty_Set) # Output: set()

# Methods of set
# Add method
my_set.add("Banana") # Adding an element to the set
print("Set after adding Banana:", my_set) # Output: Set after adding Banana: {1, 2, 3.5, 'Banana', 'Cherry', 'Apple'}

# Remove method
my_set.remove(2) # Removing an element from the set
print("Set after removing 2:", my_set) # Output: Set after removing 2: {1, 3.5, 'Banana', 'Cherry', 'Apple'}

# Set union intersection and difference
set_A = { 1, 5, 28, 76}
set_B = {2, 76, 52, 1, 28}

# Union
set_union = set_A.union(set_B)
print("Union of set_A and set_B:", set_union) # Output: Union of set_A and set_B: {1, 2, 5, 76, 52, 28}

# Intersection
set_intersection = set_A.intersection(set_B)
print("Intersection of set_A and set_B:", set_intersection) # Output: Intersection of set_A and set_B: {1, 28, 76}

# Using issubset method
set_C = {2, 28}
print("Is set_C subset of set_A?", set_C.issubset(set_A)) # Output: Is set_C a subset of set_A False.

# Using superset method
print("Is set_A superset of set_C?", set_A.issuperset(set_C)) # Output: Is set_A superset of set_C? False