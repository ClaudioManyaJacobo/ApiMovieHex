# application/controllers/movie_service.py
from domain.movies.movie_repository import MovieRepository
from domain.movies.movie import Movie
from typing import List

# Clase para gestionar las películas
class MovieService:
    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository
        
    # Método para obtener todas las películas
    def get_movies(self) -> List[Movie]:
        return self.movie_repository.get_movies()

    # Método para obtener los detalles de una película
    def get_movie_details(self, movie_id: int) -> Movie:
        return self.movie_repository.get_movie_details(movie_id)
    
    # Método para buscar películas
    def search_movies(self, query: str) -> List[Movie]:
        return self.movie_repository.search_movies(query)
