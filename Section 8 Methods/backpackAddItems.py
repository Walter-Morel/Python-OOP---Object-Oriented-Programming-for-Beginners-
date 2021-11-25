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

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print('el item no existe')
            return 0

    def has_item(self, item):
        return item in self._items


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

        