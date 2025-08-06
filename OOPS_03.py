# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Given:
#
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    def show_details(self):
        print(f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")
obj1=Bus("School Volvo",180,12)
obj1.show_details()
#
# Expected Output:
#
# Vehicle Name: School Volvo Speed: 180 Mileage: 12
