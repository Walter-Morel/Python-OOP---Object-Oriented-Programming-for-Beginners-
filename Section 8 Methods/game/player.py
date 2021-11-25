#definimos una clase para el jugador
class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    #definimos los valores por defecto
    def move_up(self, change=5):
        self.y += change

    def move_down(self, change= 5):
        self.y -= change

    def move_right(self, change= 2):
        self.x += change

    def move_left(self, change=2):
        self.x -= change


my_player = Player(5, 10)
my_player.move_up()
print(my_player.y)
    
        