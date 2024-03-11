#Exemple d'utilisation

class Film:
    def __init__(self, title, kind, duration, year):
        self.title = title
        self.kind = kind
        self.duration = duration
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Kind: {self.kind}")
        print(f"Duration: {self.duration}")
        print(f"Year: {self.year}")


class FilmDatabase:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def list_films(self):
        for film in self.films:
            film.display_info()

database = FilmDatabase()


database.add_film(Film("Harry Potter and the chamber of secrets", "Fantastic",
161, 2002))
database.add_film(Film("The Beekeeper", "Action", 105, 2024))

print("Liste des films :")
database.list_films()
