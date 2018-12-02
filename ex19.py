#we defined a function here
def vada_and_pav(no_vada,boxes_pav):
    print(f"Amount of Vada: {no_vada} and Pav: {boxes_pav}")
    print("\nWow you have many vada-pav.")

print("\n\n We can give numbers directly to function.")
vada_and_pav(20,30)

print("or , we can use variables")
vade = 10
pav = 21

vada_and_pav(vade,pav)

print("or math inside")
vada_and_pav(14+12,15-5)

print("we can combine variablels and numbers")
vada_and_pav(vade + 25, 42 - pav)

def myownfun(arg1 , arg2):
    print(f"Hello there, this is my very own function with the arguments as {arg1} and {arg2}")

myownfun("swapnil", "shreyas")
arg1 = 25

arg11 = input("put first")
arg12 = input("put second")
myownfun(arg11, arg12)

#here overloading happens.
arg1 = input("again 1st")
arg2 = input("again 2nd")
myownfun(arg1,arg2)

myownfun(vada_and_pav(15 ,20),"shahid") #Here is something wrong
