#this code is about variables
#how we can use variables in print statements is shown

Buses = 80
space_in_a_bus = 20
drivers = 25
passengers = 400
buses_not_used = Buses - drivers
buses_used = drivers
buses_capacity = buses_used * space_in_a_bus
avg_passenger_per_bus = passengers / buses_used

print("There are", Buses, ' buses available.')
print("There are only ", drivers, "drivers available.")
print("There gonna be", buses_not_used, 'empty buses today.')
print("We can transport",buses_capacity,"people today.")
print("We have", passengers, "to transport.")
print("We really need about",avg_passenger_per_bus, "persons in each bus.")
