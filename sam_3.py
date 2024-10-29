class Movie:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def watch(self):
        print(f"Today we're watching {self.name} in {self.genre} genre")

first_movie = Movie("The Substance", "Dark Comedy")

class RussianMovie (Movie):
    def __init__(self, name, genre, country = "Russia"):
        super().__init__(name, genre)

    def watch_ru(self):
        print(f"Today we're watching russian movie {self.name} in {self.genre} genre")

first_ru_movie = RussianMovie ("Brilliantovaya ruka", "Comedy")
first_ru_movie.watch_ru()
