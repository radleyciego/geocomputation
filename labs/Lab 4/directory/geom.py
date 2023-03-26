import math as mth
import random

class Geom():
    geomType = 'Generic Geometry Type'

# constructior of the class: used to initialize an object
def __init__(self):
    self.name = random.choice(['Sam','Pedro','Carlos','Maria','Khadija'])
    self.color = random.choice(['BLUE','RED','ORANGE','GREEN'])

def print_name(self):
    print('My name is ',self.name, 'and my color is ',self.color)

def makeString(self):
    return f"Name: {self.name}, Color: {self.color}, Area: {self.area()}"

class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()
        
    def area(self):
        return (self.a + self.b + self.c)** 2