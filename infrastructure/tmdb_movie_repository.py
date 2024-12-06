# infrastructure/tmdb_movie_repository.py
from domain.movie_repository import MovieRepository
from domain.movie import Movie
from .tmdb_client import TMDBClient
from typing import List

# Clase para representar un repositorio de películas de TMDB
class TMDBMovieRepository(MovieRepository):
    # Inicializamos el cliente de TMDB
    def __init__(self):
        self.tmdb_client = TMDBClient()

    # Método para obtener todas las películas
    def get_movies(self) -> List[Movie]:
        return self.tmdb_client.general_movies()

    # Método para obtener los detalles de una película
    def get_movie_details(self, movie_id: int) -> Movie:
        movie_data = self.tmdb_client.get_movie_details(movie_id)
        return self._map_movie_data(movie_data)

    # Método para buscar películas
    def search_movies(self, query: str) -> List[Movie]:
        movies_data = self.tmdb_client.search_movies(query)
        return [self._map_movie_data(movie) for movie in movies_data]

    # Método para mapear los datos de una película
    def _map_movie_data(self, movie_data: dict) -> Movie:
        video_url = self.tmdb_client.get_video_url(movie_data.get('id'))

        return Movie(
            title=movie_data.get('title', 'Unknown Title'),
            overview=movie_data.get('overview', 'No overview available'),
            release_date=movie_data.get('release_date', 'Unknown Release Date'),
            poster_path=movie_data.get('poster_path', ''),
            genres=[genre['name'] for genre in movie_data.get('genres', [])], 
            actors=self.tmdb_client.get_movie_actors(movie_data.get('id'))[:5],  
            movie_id=movie_data.get('id'),
            video_url=video_url, 
            runtime=movie_data.get('runtime', 0),
            rating=movie_data.get('vote_average', 0), 
            budget=movie_data.get('budget', 0),
            revenue=movie_data.get('revenue', 0),
            original_language=movie_data.get('original_language', 'Unknown'),
        )

