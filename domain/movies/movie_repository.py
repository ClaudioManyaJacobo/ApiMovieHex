# domain/movie_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.movies.movie import Movie

# Interfaz para el repositorio de películas
class MovieRepository(ABC):
    # Método para obtener todas las películas
    @abstractmethod
    def get_movies(self) -> List[Movie]:
        pass
    # Método para obtener los detalles de una película
    @abstractmethod
    def get_movie_details(self, movie_id: int) -> Movie:
        pass
    # Método para buscar películas
    @abstractmethod
    def search_movies(self, query: str) -> List[Movie]:
        pass
