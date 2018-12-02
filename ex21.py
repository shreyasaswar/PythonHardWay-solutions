def add(a,b):
    print(f"Adding {a} and {b}\n")
    return a + b

def sub(a,b):
    print(f"Substracting {b} from {a}\n")
    return a - b

def mul(a,b):
    print(f"Multiplying {a} with {b}\n")
    return a * b

def div(a,b):
    print(f"Dividing {a} by {b}\n")
    return a/b

age = add(17,4)
height = sub(30,9)
wt = mul(7,3)
iq = div(100,1)

print("Here it is : \n")
print(f"Age is {age}, height is {height}, wt is {wt} and iq is {iq}")

what = add(age,sub(height, mul(wt, div(iq,2))))
print(f"so the puzzle --> {what}")
