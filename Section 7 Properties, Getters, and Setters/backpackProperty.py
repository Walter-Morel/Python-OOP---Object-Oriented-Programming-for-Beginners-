class Backpack:

    def __init__(self):
        self._items = []

    @property
    def itmes(self):
        print('calling to getter')
        return self._items

    @itmes.setter
    def items(self, newitems):
        if isinstance(newitems, list):
            print('calling to setters')
            self._items = newitems
        else:
            print('por favor añade un item valido')
            

my_backpack = Backpack()            
print(my_backpack.items)

#añadiendo valor a la lista
my_backpack.items = ['water bottle', 'sleeping bag']
print(my_backpack.items)