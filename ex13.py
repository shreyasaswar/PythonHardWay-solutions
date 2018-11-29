#from sys library or package import argv module
from sys import argv

#It is unpacking, elements in the argv list are assigned to varibales on left
script, first, second, third= argv

print("The script is called :", script)
print("Your first variable is ", first)
print("your second variable is", second)
print("your third variable is ", third)
