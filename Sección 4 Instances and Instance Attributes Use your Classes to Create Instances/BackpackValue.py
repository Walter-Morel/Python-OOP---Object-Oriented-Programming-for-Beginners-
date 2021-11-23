class  Backpack:
    def __init__(self, items, color='green'):
        self.items = items
        self.color = color


my_backpack = Backpack('pencil', 'Blue')
print(my_backpack.items)
print(my_backpack.color)
#Una instancia es independiente de la otra
my_backpack.color = 'Red'
my_backpack.items = 'Regla'
print(my_backpack.items)
print(my_backpack.color)
