class Animal:
    group = "Mammal"
    leg_count = 4

    # default constructor
    def __init__(self):
        self.name = "Unkown"

class vehicle:

    can_fly = False
    tire_count= 4
    # parameterized constructor
    def __init__(self,make):
        self.make = make
    def set_tire_count(self, count):
        self.tire_count = count

    def set_flyable(self, cfly):
        self.can_fly = cfly

class Human:

    leg_count = 4
    group = "Black"
    # Default constructor
    def __init__(self):
        self.name = "Negroid"
animal = Animal()
print("Animal:", animal.name, animal.group)

Toyota = vehicle ("Toyota")
print("*\nVehicle:", Toyota.make, Toyota.can_fly)

Honda = vehicle ("Honda")
print("*\nVehicle:", Honda.make, Honda.can_fly)

Lexus = vehicle ("Lexus")
print("*\nVehicle:", Lexus.make, Lexus.can_fly)

Human = Human()
print("Human:", Human.name, Human.group)

plane = vehicle("Aeroplane")
plane
print("*\nVehicle:" , plane.make, plane.can_fly)