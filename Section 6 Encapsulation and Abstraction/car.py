class   Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year #con un guion bajo convertimos un atributo en privado


my_car = Car('Porsche', '911 carrera', 2020)
print(my_car._year) #Accedemos a un atributo privado colocando solo un guion bajo por delante
        