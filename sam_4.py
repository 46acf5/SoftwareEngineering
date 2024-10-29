class Movie:
    def __init__(self, name, genre):
        self._name = name
        self.__genre = genre

    def watch(self):
        print(f"Today we're watching {self._name} in {self.__genre} genre")

first_movie = Movie("The Substance", "Dark Comedy")
print(first_movie._name)
print(first_movie.__genre)
first_movie.watch()
