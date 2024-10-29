class Movie:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def watch(self):
        print(f"Today we're watching {self.name} in {self.genre} genre")

first_movie = Movie("The Substance", "Dark Comedy")

class WorldMovie (Movie):
    def __init__(self, name, genre, country):
        super().__init__(name, genre)
        self.country = country

    def watch_ru(self):
        print(f"Today we're watching russian movie {self.name} in {self.genre} genre, made in {self.country}")

first_ru_movie = WorldMovie ("Brilliantovaya ruka", "Comedy", "Russia")
first_ru_movie.watch_ru()
