"""
class Point():  #OOP creating a Class representing  a point
    def __init__(self, input1, input2): #Define a function init that accepts 2 inputs and stores them in a property x and y
        self.x = input1
        self.y = input2

p = Point(7, 19)
print(p.x)
print(p.y)

"""

class Flight():
    def __init__(self, capacity): #1st method
        self.capacity = capacity
        self.passengers = []               #creating a list of passengers
    def add_passenger(self, name): #2nd method to add passengers
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self): #3rd method to show us how many seats there are
        return self.capacity - len(self.passengers)
        

flight = Flight(5)            #book a flight of 5 passengers(capacity)

people = ["Mwendwa", "Mutunga", "Victor", "Mutinda", "Kioko", "Daniel", "Cozy"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")

else:
    print(f"No available seats for {person}")

