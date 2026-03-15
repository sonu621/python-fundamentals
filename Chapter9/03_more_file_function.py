file = open("file.txt")

lines = file.readlines()
while(lines != ""):
    print(lines)
    lines = file.readline()
file.close()


## Modes of openinf a file:

'''
r - open for reading
w - open for writing
a - open for appending
+ - open for updating
'rb' - will open for read in binary mode.
'rt' - will open for read in text mode.
'''