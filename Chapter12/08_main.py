# ----------------- If __name__ == '__main__' in Python --------------

# In Python, __name__ is a special built-in variable.

# When a Python file is run directly, __name__ is set to "__main__".

# When a Python file is imported as a module into another file, __name__ is set to the module's name

# __name__ == "__main__" → File is running directly
# __name__ != "__main__" → File is imported

from module import myFunction

if __name__ == "__main__":
    # If this code is directly executed by running the file its present file.
    print("We are directly running this code!")
    myFunction()