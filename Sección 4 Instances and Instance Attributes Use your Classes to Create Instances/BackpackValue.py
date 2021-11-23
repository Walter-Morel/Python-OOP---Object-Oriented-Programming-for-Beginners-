class  Backpack:
    def __init__(self, color='green'):
        self.items = []
        self.color = color


my_backpack = Backpack('Blue')
print(my_backpack.color)
my_backpack.color = 'Red'
print(my_backpack.color)
