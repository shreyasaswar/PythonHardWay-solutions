from sys import argv
script, input = argv

def read(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def line(linec, f):
    print(linec,f.readline(), end="")

current = open(input)

print("First we'll print the whole file")
read(current)

print("we'll go back like tape recorder")
rewind(current)

print("go to line")

currentl = 1
line(currentl, current)

currentl += 1
line(currentl, current)

currentl += 1
#currentl = currentl + 1
line(currentl, current)
