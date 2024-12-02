# domain/movie.py
class Movie:
    def __init__(self, title, overview, release_date, poster_path, genres, actors):
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.poster_path = poster_path
        self.genres = genres
        self.actors = actors

    def __repr__(self):
        return f"<Movie {self.title}>"