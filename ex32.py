the_count = [1,2,3,4,5]
fruits = ['apple','grapes','watermellon','oranges','pears']
change = [1,'dime',2,'pennies',3,'quarters']

for number in the_count:
    print(f"This is count {number}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range(10,16):
    print(f"Adding {i} to the list.")
    elements.append(i)

print("\n We'll print all the elements we've just added: \n")
for i in elements:
    print(f"Element - {i}")
