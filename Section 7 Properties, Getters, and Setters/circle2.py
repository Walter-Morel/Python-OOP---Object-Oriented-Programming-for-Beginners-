class Circle:
    #La constante se define en mayusculas
    VALID_COLOR = ('red', 'blue', 'green') #CONSTANTE QUE HEMOS DEFINIDO PARA EL SET_COLOR

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, newradius):
        if isinstance(newradius, int) and newradius > 0:
            self._radius = newradius
        else:
            print('por favor ingrese un valor valido')
    #añadiendo propiedad a radius
    radius = property(get_radius ,set_radius)

    #para añadir una propiedad a color, debemos definir un get y set
    def get_color(self):
        return self._color

    def set_color(self, newcolor): #debemos definir una constante para validar si el color existe en nuestra lista
        if newcolor in Circle.VALID_COLOR:
            self._color = newcolor
        else:
            print('Por favor ingrese un color valido.')
    #añadimos propiedades al color
    color = property(get_color, set_color)

#program
my_circle = Circle(10, 'blue')#instance

#imprimimos el radio
print(my_circle.radius)
#actualizamos el valor de radio
my_circle.radius = 16
print(f'el nuevo valor de radio es {my_circle.radius}')

#imprimimos el color
print(my_circle.color)
#actualizamos el valor de color
my_circle.color = 'black'
print(f'el nuevo color es: {my_circle.color}')


        