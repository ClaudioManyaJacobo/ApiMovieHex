# app/services/movie_service.py
from infrastructure.api_service import MovieAPIService

class MovieService:
    def __init__(self):
        self.api_service = MovieAPIService()

    def get_movies(self):
        movies = self.api_service.get_movies()  # Asignamos directamente la lista de películas
        return movies

    def get_movie_details(self, movie_id):
        return self.api_service.get_movie_details(movie_id)
    
    