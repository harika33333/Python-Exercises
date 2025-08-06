# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self,speed,mileage):
        self.max_speed=speed
        self.mileage=mileage
my_bike=Vehicle(120,70)
print(my_bike.max_speed)

