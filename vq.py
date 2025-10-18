class Vehicle:
    def describe(self):
        print("This is a generic vehicle")
class Truck(Vehicle):
    print("This is a sporty Truck")
class Motorcycle(Vehicle):
    print("This is a fast motorcycle")
# make a objects
vehicle = Vehicle()
truck = Truck()
motorcycle = Motorcycle
