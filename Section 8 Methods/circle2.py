class Circle:

    def __init__(self, radius):
        self.radius = radius

    def find_diameter(self):
        return self.radius * 2


my_circle = Circle(5)        
#para llamar un metodo escribimos la siguiente sintaxis.
diameter = my_circle.find_diameter()
print(diameter)
        