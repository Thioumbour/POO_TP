#Exemple sans SRP

class Film:
    def __init__(self, title, kind, duration, year):
        self.title = title
        self.kind = kind
        self.duration = duration
        self.year = year

class FilmDatabase:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def search_film_by_title(self, title):
        return [film for film in self.films if film.title == title]

    def search_film_by_kind(self, kind):
        return [film for film in self.films if film.kind == kind]

    def search_film_by_year(self, year):
        return [film for film in self.films if film.year == year]
        
    def display_film_info(self, film):
        print(f"Title: {film.title}")
        print(f"Kind: {film.kind}")
        print(f"Duration: {film.duration}")
        print(f"Year: {film.year}")


#Refactorisation de l'exmple avec SRP

class Film:
    def __init__(self, title, kind, duration, year):
        self.title = title
        self.kind = kind
        self.duration = duration
        self.year = year

class FilmDatabase:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def search_film_by_title(self, title):
        return [film for film in self.films if film.title == title]

    def search_film_by_kind(self, kind):
        return [film for film in self.films if film.kind == kind]

    def search_film_by_year(self, year):
        return [film for film in self.films if film.year == year]
        
class FilmInfo:
     def display_film_info(self, film):
        print(f"Title: {film.title}")
        print(f"Kind: {film.kind}")
        print(f"Duration: {film.duration}")
        print(f"Year: {film.year}")
