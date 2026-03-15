a = (1,)
print(type(a))

b = (1, 45, False, 45, "Rohan", "Sohan")
print(b.count(1)) # Output: 1
print(b.index("Sohan")) # Output: 5
print( 45 in b) # Output: True
print("Sonu" in b) # Output: False
print(b[2]) # Output: False