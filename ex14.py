from sys import argv

script, user_name = argv
prompt = '-->'

print(f"Hi {user_name}, I'm your {script} ! ,  Shocked ?")
print("Answer me few questions .")
print(f"Do you like Shreyas, {user_name} ?")
like = input(prompt)

print(f"Where do you live, {user_name} ?")
live = input(prompt)

print(f"What kind of computer do you have, {user_name} ? ")
computer = input(prompt)

print(f"""
Okay, so you said {like} about liking Shreyas,
also you said that you live in {live}, which is a nice place
but really you have {computer} ? , Nice !
""")
