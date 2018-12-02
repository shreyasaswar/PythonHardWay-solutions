#i = 0
#numbers = []

def myfun(a,b):
    i = 0
    numbers = []
    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += b
        print("Numbers now ", numbers)
        print(f"At the bottom i is {i}")

#a = int(input("Enter a number"))
myfun(int(input("Enter a number.")),int(input("Enter how much increment")))

#print("The numbers:")

#for num in numbers:
    #print(num)
