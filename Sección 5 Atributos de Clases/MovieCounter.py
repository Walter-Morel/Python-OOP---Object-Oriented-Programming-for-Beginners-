class Movie:

    id_counter = 1

    def __init__(self, title, rating):
        self.id = Movie.id_counter
        self.title = title
        self.rating = rating

        Movie.id_counter += 1


my_movie = Movie('Paul', 5.5)
your_movie = Movie('Titanic', 5.6)

print('Movies.')
print('id: {} | title: {} | rating: {}'.format(my_movie.id, my_movie.title, my_movie.rating))
print('id: {} | title: {} | rating: {}'.format(your_movie.id, your_movie.title, your_movie.rating))
