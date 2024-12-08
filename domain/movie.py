# domain/movie.py
# Clase para representar una película
class Movie:
    def __init__(self, title, overview, release_date, poster_path, backdrop_path, genres, actors, movie_id=None, video_url=None, 
                 runtime=None, rating=None, budget=None, revenue=None, original_language=None, director=None):
        self.title = title # Título de la película
        self.overview = overview # Sinopsis de la película
        self.release_date = release_date # Fecha de lanzamiento
        self.poster_path = poster_path # Ruta del póster
        self.backdrop_path = backdrop_path # Ruta del fondo de pantalla
        self.genres = genres # Géneros de la película
        self.actors = actors # Actores de la película
        self.id = movie_id # ID de la película
        self.video_url = video_url # URL del video
        self.runtime = runtime # Duración de la película
        self.rating = rating # Calificación de la película
        self.budget = budget # Presupuesto de la película
        self.revenue = revenue # Ingresos de la película  
        self.original_language = original_language # Idioma original de la película
        self.director = director
    def __repr__(self):
        return f"<Movie {self.title}>"
