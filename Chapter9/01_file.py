# Types Of Files:
## There are two types of files:

### 1. Text files(.txt, .c. etc)
### 2. Binary files(.jpg, .dat, etc.)

## Python has a lot of function for reading, updating and deleting files.

## Opening a File":-
### Python has an open() function for opening files. It takes 2 parameters: filename and mode.


f = open("file.txt", "r")
data = f.read()
print(data)
f.close()