# infrastructure/api_service.py
from .tmdb_client import TMDBClient
from domain.movie import Movie

class MovieAPIService:
    def __init__(self):
        self.tmdb_client = TMDBClient()

    def get_movies(self):
        # Obtener películas populares
        movies_data = self.tmdb_client.get_sci_fi_movies()
        movies = []

        for movie_data in movies_data:
            movie_id = movie_data['id']
            details = self.tmdb_client.get_movie_details(movie_id)
            credits = self.tmdb_client.get_movie_credits(movie_id)

            genres = [genre['name'] for genre in details.get('genres', [])]
            actors = [actor['name'] for actor in credits.get('cast', [])[:5]]  # Primeros 5 actores

            movie = Movie(
                title=movie_data['title'],
                overview=movie_data['overview'],
                release_date=movie_data['release_date'],
                poster_path=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}",
                genres=genres,
                actors=actors
            )
            movies.append(movie)

        return movies
