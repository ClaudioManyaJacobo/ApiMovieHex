# domain/movie.py
# Clase para representar una película
class Movie:
    def __init__(self, title, overview, release_date, poster_path, genres, actors, movie_id=None, video_url=None, 
                 runtime=None, rating=None, budget=None, revenue=None, original_language=None, last_update=None):
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.poster_path = poster_path
        self.genres = genres
        self.actors = actors
        self.id = movie_id
        self.video_url = video_url
        self.runtime = runtime
        self.rating = rating
        self.budget = budget
        self.revenue = revenue
        self.original_language = original_language
        self.last_update = last_update

    def __repr__(self):
        return f"<Movie {self.title}>"
