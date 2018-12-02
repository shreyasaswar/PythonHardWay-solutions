def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1} and arg2:{arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")

def print_one(khitri):
    print(f"See the only argument {khitri}")

def print_none():
    print("I got nothing.")

print_two("Shreyas","Swapnil")
print_two_again("Anu","Sonu")
print_one('Aswar')
print_none()
