class Geom():
    geomType = 'Generic Geometry Type'

class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()
        
    def area(self):
        return (self.a + self.b + self.c)** 2