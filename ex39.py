list = ['p','q','r','s']
print("Lets print the element in the list which is on 1st index:")
print(list[1]) #it will print q
print("Lets print the whole list")
print(list)

dict = {'a':'apple', 'b':'ball', 'c':'cat', 'd':'dog', '1':'anjangaon', '2':'amravati'}
print("We'll first print through key")
#dictionary is a key value pair
print(dict['a'])
print(dict['d'])
dict['e'] = 'elephant'
print(dict['e'])

states = {'MH':'Maharashtra', 'GJ':'Gujrat', 'AP':'Andhra Pradesh', 'RJ':'Rajasthan','VB':'Vidarbha'}

cities = {'MH':'Mumbai','GJ':'Surat','AP':'Amravati', 'RJ':'Jaipur', 'VB':'Nagpur'}

print('=' * 25)
print("Maharashtra state has:", cities['MH'])
print("Vidarbha state has:", cities['VB'])

print('=' * 20)
print("GJ is:", states['GJ'])
print("RJ is:", states['RJ'])

print('*' * 25)
for abr ,city in cities.items():
    print(f"{abr} is abbrevation for {city}")
