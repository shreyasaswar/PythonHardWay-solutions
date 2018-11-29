#it imports argv function from the module sys
from sys import argv

#unpacks the argv in script and tx15
#it means you have to give two arguments while running the script
script, tx15 =argv

#open function with parameter tx15 , opens the file and keeps it in variable txt
txt = open(tx15)

print(f"Here is your file {tx15}")
print(txt.read())
#we call read() function on txt variable without any paramter
#we print it all
txt.close()

print("type the filename again:")
file_again = input("==>")
#filename is obtained from user by input() function
#we prompt input with ==>

#filename from user is opend and stored in varibale txt_again
txt_again = open(file_again)
input(txt_again.read())
#we called function read() on txt_again.
txt_again.close()
