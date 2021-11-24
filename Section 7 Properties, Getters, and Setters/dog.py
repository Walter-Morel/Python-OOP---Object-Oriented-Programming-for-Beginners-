#Setters
class Dog:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            print('Por favor ingrese un nombre valido')

#Program
my_dog = Dog('Nora', 8)  #<--- instance          
print('My dog is: {}'.format(my_dog.get_name()))

#my_dog.set_name('Norita') #<---- instance
my_dog.set_name('Norita434234') #<---- instance | en la definicion set_name se indico que tiene que haber una cadena para que esa condicion se cumpla, si añadimos un numero al final
#la condicion no se cumple
print('Her new name is: {}'.format(my_dog.get_name()))



        