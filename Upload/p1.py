# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:25:04 2020

@author: MAYANK SHAW
"""

class Vehicle:
    def __init__(self, license_no):
        self.license_no = license_no
    
    def give_license(self):
        return self.license_no

class Truck(Vehicle):
    def __init__(self, license_no, tires, color, price, name):
        self.license_no = license_no
        self.tires = tires
        self.color = color
        self.price = price
        self.name = name
        
    def calculate_comission(self):
        return 0.1 * self.price
    
    def details(self):
        print(f"The name is {self.name} , of {self.color} color and price : RS {self.price}")
        
t1 = Truck("WB89 7856A", 10, "orange", 100000, "Ashok Leyland Nixon")
t2 = Truck("TN76 BF6G7", 8, "white", 80000, "Tata Jayanti")

t1.details()
print(f"Comission for {t1.name} is RS {t1.calculate_comission()}")
print(f"License number: {t1.give_license()}")
t2.details()
print(f"Comission for {t2.name} is RS {t2.calculate_comission()}")
print(f"License number: {t2.give_license()}")