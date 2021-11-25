class Backpack:

    def __init__(self):
        self._items = []


    @property
    def items(self):
        return self._items

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print('please add new item')

    def multiple_items(self, items): #definimos un metodo para agregar multiples veces un item
        for item in items:
            self.add_item(item)

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print('el item no existe')
            return 0

    def has_item(self, item):
        return item in self._items
    #Definiendo el metodo show items para que me muestre todos los items de la mochila
    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)


#program
my_backpack = Backpack()
print(my_backpack.items)
#añadimos items
my_backpack.add_item('water bottle')
print(my_backpack.items)
my_backpack.add_item('sleeping bag')
print(my_backpack.items)
my_backpack.add_item('pencil')
print(my_backpack.items)

#removemos un item
my_backpack.remove_item('pencil')
print(my_backpack.items)
#comprobamos si un item en especifico existe en nuestra mochila
has_pencil = my_backpack.has_item('pencil')
print(f'Existe la bolsa de dormir en nuestra mochila?: {has_pencil}')

my_backpack.add_item('candy')
print('not sorted:')
my_backpack.show_items()

print('sorted:')
my_backpack.show_items(True)

#agregamos varios items utilizando el metodo multiple_items
my_backpack.multiple_items(['pencil', 'carrot', 'anana'])
print(my_backpack.items)


        