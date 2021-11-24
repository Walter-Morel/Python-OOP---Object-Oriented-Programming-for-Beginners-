#Getters
class  Movie:

    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    
    def get_title(self):
        return self._title


my_movie = Movie('Paul', 4.3)

print('Mi pelicula favorita es: {}'.format(my_movie.get_title()))
        