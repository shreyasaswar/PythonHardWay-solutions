types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said {x}")
print(f"I also said that {y}")

hilarious = False
joke_evaluation =  "Isn't that joke so funny?!{}"

#This is how we can format string in a different style
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with right side."

#This is concatenation of strings
print (w + e)
