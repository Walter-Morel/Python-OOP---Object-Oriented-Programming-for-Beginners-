class Backpack:

    def __init__(self, items):
        self._items = []

    def get_items(self):
        return self.get_items

    def set_items(self, newitem):
        if isinstance(newitem, list):
            self._items = newitem
        else:
            print('Por favor añade un item valido')


my_backpack = Backpack()
print(my_backpack.get_items())           
        