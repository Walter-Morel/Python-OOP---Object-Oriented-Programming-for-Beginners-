class Movie:
    def __init__(self, tittle, year, language, rating):
        self.tittle = tittle
        self.year = year
        self.language = language
        self.rating = rating


favorite_movie = Movie('Paul', 1997, 'English', 4.6)

print(favorite_movie.tittle)
print(favorite_movie.year)
print(favorite_movie.language)
print(favorite_movie.rating)
        