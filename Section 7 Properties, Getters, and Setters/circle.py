class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, newRadius):
        if isinstance(newRadius, float) and newRadius > 0:
            self._radius = newRadius
        else:
            print('Por favor ingresa un valor valido para el radio.')

#program            
my_circle = Circle(31) #<--- instance
print(my_circle.get_radius())

my_circle.set_radius(0)#<--- instance
print(my_circle.get_radius())
        