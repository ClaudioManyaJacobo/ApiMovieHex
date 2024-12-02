# app/services/movie_service.py
from infrastructure.api_service import MovieAPIService

class MovieService:
    def __init__(self):
        self.api_service = MovieAPIService()

    def get_movies(self):
        return self.api_service.get_movies()
