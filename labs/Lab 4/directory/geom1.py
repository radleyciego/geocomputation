import math as mth
import random

class Geom():
    geomType = 'Generic Geometry Type'

    def __init__(self):
        self.name = random.choice(['Sam','Pedro','Carlos','Maria','Khadija'])
        self.color = random.choice(['BLUE','RED','ORANGE','GREEN'])

    def print_name(self):
        print('My name is ',self.name, 'and my color is ',self.color)

    def makeString(self):
        return f"Name: {self.name}, Color: {self.color}, Area: {self.area()}"

class Circle(Geom):
  
  def __init__ (self, r):
    self.radius = r
    super().__init__()
  def area(self):
     return mth.pi * self.radius **2
  
class Square(Geom):
  def __init__ (self, s):
    self.side = s
    super().__init__()
  def area(self):
     return self.side **2

class Tri(Geom):
    def __init__(self, b, h):
        self.b = b
        self.h = h
        super().__init__()
    def area(self):
        return (self.b * self.h)*0.5