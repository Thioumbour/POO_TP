#Exemple sans LSP

class Film:
    def __init__(self, title, kind, duration, year):
        self.title = title
        self.kind = kind
        self.duration = duration
        self.year = year

    def play(self):
        print(f"Playing {self.title} - {self.duration} minutes")

class StreamingFilm(Film):
    def __init__(self, title, duration, kind, platform):
        super().__init__(title, duration, kind)
        self.platform = platform

    def stream(self):  
        print(f"Streaming {self.title} - Available on {self.platform}")

#Refactorisation de l'exemple avec LSP

class Film:
    def __init__(self, title, kind, duration, year):
        self.title = title
        self.kind = kind
        self.duration = duration
        self.year = year

    def play(self):
        print(f"Playing {self.title} - {self.duration} minutes")

class StreamingFilm(Film):
    def __init__(self, title, duration, kind, platform):
        super().__init__(title, duration, kind)
        self.platform = platform

    def play(self):
        print(f"Streaming {self.title} - Available on {self.platform}")

class DVDFilm(Film):
    def __init__(self, title, duration, kind, region_code):
        super().__init__(title, duration, kind)
        self.region_code = region_code

    def play(self):
        print(f"Playing DVD {self.title} - Region Code: {self.region_code}")
