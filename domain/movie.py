# domain/movie.py
class Movie:
    def __init__(self, title, overview, release_date, poster_path, genres, actors, movie_id=None, video_url=None):
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.poster_path = poster_path
        self.genres = genres
        self.actors = actors
        self.id = movie_id
        self.video_url = video_url  # Nuevo atributo para el video

    def __repr__(self):
        return f"<Movie {self.title}>"
    
