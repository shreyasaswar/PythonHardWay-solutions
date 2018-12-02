from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that then press CTRL-C")
print("If you want to continue then hit return")

input("Now do what you want")

print("Hurray , you want erase")
print("opening file............")
target = open(filename,'r+')

print("see the file contents last time")
print(target.read())

print("Truncating the file, see you soon")
target.truncate()

print("Done , now tell me what to enter in file")

line1 = input("Tell me the first line.")
line2 = input("Second line")
line3 = input("last one")

print("wait I'll write it")

target.write(f"{line1}\n{line2}\n{line3}")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("finally we're gonna close it.")
target.close()
