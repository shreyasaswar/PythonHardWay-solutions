#variables people ,cars , trucks assigned some values
people = 30
cars = 40
trucks = 40

#if statement is used with condition (cars>people)
if cars > people:
    #block of code aka branch which will be executed only when the condition in if statement is true
    print("We should take the cars.")
#elif is the statement which is executed if , if condition is false
elif cars < people:
    print("We shouldnt take the cars.")
#if and elif is false then finally else is executed
else:
    print("We can not decide.")

if trucks > cars:
    print("Thats too many trucks.")
elif trucks < cars:
    print("Maybe we should take the trucks.")
else:
    print("We can't decide.")

if people > trucks:
    print("Alright, lets just take the trucks.")
else:
    print("Fine let's stay home then.")
