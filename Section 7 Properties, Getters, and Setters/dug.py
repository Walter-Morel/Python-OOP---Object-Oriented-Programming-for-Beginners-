#property
import time

class Dog:

    def __init__(self, age):
        self._age = age

    def get_age(self):
        print('Run getter...')
        return self._age
        time.sleep(2)

    def set_age(self, age):
        print('Running setters...')
        if isinstance(age, int) and 0 < age < 30:
            self._age = age
        else:
            print('Por favor ingrese una edad valida.')
        
    age = property(get_age, set_age)


#program
my_dog = Dog(9)
print(my_dog.age)

my_dog.age = my_dog.age + 1
print(f'la nueva edad de mi perro es {my_dog.age}')
        