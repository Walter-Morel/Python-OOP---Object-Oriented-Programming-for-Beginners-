'''- Explique por qué se prefiere la sintaxis @property en Python sobre los getters, setters y property ()

- Refactorice la clase a continuación para trabajar con propiedades. Primero, haga que todos los atributos estén protegidos.
Luego, agregue captadores y definidores para los tres atributos y cree dos versiones de la clase: una con la sintaxis property () y otra con la sintaxis @property. '''

class BouncyBall:

    def __init__(self, price, size, brand):
	        self._price = price #protegemos los atributos 
	        self._size = size 
	        self._brand = brand
    #definimos los getters y setters para Price.
    #Property version 1
    def get_price(self):
        return self._price

    def set_price(self, newPrice):
        if isinstance(newPrice, int) and newPrice > 10:
            print('Calling to Setters Price')
            self._price = newPrice
        else:
            print('Please enter to valid price.')
        
        #price = property(get_price, set_price
                 
    #propery version 2
        @property
        def price(self):
            print('Calling to Getter Price')
            return self._price          
        @price.setter
        def price(self, newPrice):
            if isinstance(newPrice, int) and newPrice > 10:
                print('Calling to setters Price')
                self._price = newPrice
            else:
                print('Please enter to valid price.')

    #definimos los getters y setters para Price.
    #Property version 1
    def get_size(self):
        return self._size

    def set_size(self, newSize):
        if isinstance(newSize, int) and newSize > 2:
            print('Calling to Setters Size')
            self._size = newSize
        else:
            print('Please enter to valid size.')

        #size = property(get_size, set_size)
    #property version 2
        @property
        def size(self):
            print('Calling to getters size')
            return self._size
        @size.setter
        def size(self, newSize):
            if isinstance(newSize, int) and newSize > 2:
                print('Calling to setters Size')
                self._price = newSize
            else:
                print('Please enter to valid Size.')
    #definimos los getters y setters para Brand.
    #Property version 1
    def get_brand(self):
        return self._brand

    def set_brand(self, newBrand):
        if isinstance(newBrand, bool) and newBrand is True:
            print('Calling to Setters Brand')
            self._brand = newBrand
        else:
            print('Please enter to valid brand.')

        #brand = property(get_brand, set_brand)
    #property version 2
        @property
        def brand(self):
            print('Calling to getters brand')
            return self._brand
        @brand.setter
        def brnad(self, newBrand):
            if isinstance(newBrand, bool) and newBrand is True:
                print('Calling to setters Brand')
                self._brand = newBrand
            else:
                print('Please enter to valid Brand.')
    



#program
my_bouncyBall = BouncyBall(0, 50, True)             
print(f'My Bouncy ball price is: {my_bouncyBall._price}, size is {my_bouncyBall._size} and brand is {my_bouncyBall._brand}')
            


            
