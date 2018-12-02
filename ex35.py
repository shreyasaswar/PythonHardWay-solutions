from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take ?")

    choice = input("--->>")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man learn to type binary Numbers")

    if how_much < 50:
        print("Nice , you're not greedy. Bye")
        exit(0)
    else:
        dead("you greedy bastard")


def bear_room():
    print("""
        There is a bear here.
        The bear has bunch of honey.
        The fat bear is infront of another door.
        how are going to move the fat bear?
    """)
    bear_moved = False

    while True:
        choice = input("---->>")

        if choice == "take honey":
            dead("the bear takes his honey back by killing you.")

        elif choice == "taunt bear" and not bear_moved:
            print("congo bear moved")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("His pissed off !")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("WHat ???")

def danger_room():
    print("""
    HAVE You EVER  heard about Cthulhu
    he , it , whatever stares at you and you go insane
    Do you flee for your life or eat your head ?

    """)

    choice = input("___>>")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("tasty head")
    else:
        danger_room()

def dead(why):
    print(why, "Good job now Bye!")
    exit(0)
def start():
    print("""
    You are in a dark room.
    There is a door to your right and left
    which one you take ?
    """)

    choice = input("===>>")

    if "left" in choice:
        bear_room()
    elif "right" in choice:
        danger_room()
    else:
        print("when you try something else you die !")

start()
