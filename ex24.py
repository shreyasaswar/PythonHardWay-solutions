print("Lets revise everything.")
print('You\'d need to know \'bout escapes with \\ that do :')
print('\n newline and \t tabs.')

poem = '''
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n \t where there is none.
'''

print("====================")
print(poem)
print("====================")


five = 10 - 2 + 3 - 6
print(f"This should be five : {five}")

def secret_for(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_for(start_point)


print("with a starting point of: {}".format(start_point))

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do this , this way:")
formula = secret_for(start_point)

print("We'd have {}beans, {}jars , and {} crates".format(*formula))
