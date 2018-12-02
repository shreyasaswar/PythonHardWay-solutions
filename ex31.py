print(""" You enter in a room with two doors.
Do you go through door1 or door2?
""")

door = input("=====>")

if door == "1":
    print(""" There's a giant bear eating a cheescake.
        What you do ?
        1. Eat the cake.
        2. Scream.
    """)

    door1 = input("---->>")
    if door1 == "1":
        print("Now the bear is hungry , he eats you. Good JOB !")
    elif door1 == "2":
        print("Now the bear knows you are there, he eats you. Good Job !! ")
    else:
        print(f"Well you think out of the box, '{door1}' is impressive !")

elif door == "2":
    print("""
    You stare at the endless abyss at Cthulhu's retina.
    1. Blueberries.
    2.Yellow jacket clothespin.
    3. Understanding revolvers yelling melodies.
    """)

    door2 = input("-->>")
    if door2 == "1" or door2 == "2":
        print("You survive!")
    else:
        print("You die!")

else:
    print("You falter and fall on a knife and die. Good job !")
