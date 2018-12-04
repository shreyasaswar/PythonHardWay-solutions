class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_it(self):
        for line in self.lyrics:
            print(line)

Channa_Mereya = Song(["Accha chalta hoon",
"duwoon me yaad rakhna",
"mere jikra ka jubaan pe suwaad rakhna"])

Perfect = Song(["Loving can hurt",
"loving can hurt sometime",
"but its the only ting that I know",
"when it gets hard"])

cat = ["Smelly cat","Smelly cat","What are they feeding you ?",
"Smelly cat Smelly cat its not your fault."]

Smelly_cat = Song(cat)

Wake_me = Song('''Fill my way
through the darkness
guided by beating heart
i dont know where the journey ends
but i know where to start''')

Channa_Mereya.sing_it()

Perfect.sing_it()

Smelly_cat.sing_it()

Wake_me.sing_it()
