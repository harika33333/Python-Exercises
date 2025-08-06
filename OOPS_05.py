# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
#
# Use the following code for this exercise.
#
# Expected Output:
#
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
class Vehicle:
    color="white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
# print(Vehicle.color)
bus=Bus("School volvo",180,12)
car=Car("audi q5",173,18)
print(f"Color: {Vehicle.color}, Vehicle name: {bus.name}, Speed: {bus.max_speed}, Mileage: {bus.mileage}")
print(f"Color: {Vehicle.color}, Vehicle name: {car.name}, Speed: {car.max_speed}, Mileage: {car.mileage}")

