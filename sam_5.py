class Movie:
    def watch(self):
        pass

class MovieByItsGenre(Movie):
    def __init__(self, name, genre):
        self._name = name
        self._genre = genre

    def watch(self):
        print(f"Today we're watching {self._name} in {self._genre} genre")

class MovieByItsYear(Movie):
    def __init__(self, name, year):
        self._name = name
        self._year = year

    def watch(self):
        print(f"Today we're watching {self._name} of the {self._year} year")

films = [MovieByItsGenre("Interstellar", "Adventure Epic"),
         MovieByItsYear("Mad Max: Fury Road", 2015)]
for film in films:
    print(film.watch())
