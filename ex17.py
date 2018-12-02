#this snippet is for copying one file to other 
from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()
#indata = in_file.read()

print(f"Lenght of the file is {len(indata)} bytes long. ")

print(f"Does the output file exists ? {exists(to_file)}")
print("hit enter to continue")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("done")

out_file.close()

#in_file.close()
