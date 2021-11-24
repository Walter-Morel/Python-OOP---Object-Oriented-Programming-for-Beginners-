#decorator
class Movie:

    def __init__(self, title, rating):
        self._title = title
        self._rating = rating
    #creamos un decorador para agregar un getter y un setter
    @property
    def rating(self):
        print('llamando al getter')
        return self._rating
    @rating.setter
    def rating(self, newrating):
        if isinstance(newrating, float) and 1.0 <= newrating <= 5.0:
            print('llamando al setters')
            self._rating = newrating
        else:
            print('ingresa un valor valido.')


#program
favorite_movie = Movie('titanic', 4.3)        
print(favorite_movie._rating)

#cambiando el valor de rating
favorite_movie.rating = 10
print(favorite_movie.rating)
    
        