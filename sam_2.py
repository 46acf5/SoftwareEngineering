class Movie:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def watch(self):
        print(f"Today we're watching {self.name} in {self.genre} genre")

first_movie = Movie("The Substance", "Dark Comedy")
first_movie.watch()
