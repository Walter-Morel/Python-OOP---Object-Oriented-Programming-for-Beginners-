class Movie:

    movie_id = 1

    def __init__(self, id, name, year, rating):
        self._id = Movie.movie_id
        self.name = name
        self.year = year
        self.rating = rating

        Movie.movie_id += 1


my_movie = Movie('Titanic', 1997, 5.6)
your_movie = Movie('Paul', 2000, 6.5 )

print(my_movie.movie_id)
print(your_movie.movie_id)