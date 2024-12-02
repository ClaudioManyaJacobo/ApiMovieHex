# infrastructure/tmdb_client.py
import requests
from app.config import Config

class TMDBClient:
    def __init__(self):
        self.api_key = Config.API_KEY
        self.base_url = Config.BASE_URL
        self.language = Config.LANGUAGE

    # Obtener películas de Ciencia Ficción
    def get_sci_fi_movies(self):
        genre_id = 878  # ID de Ciencia Ficción
        url = f"{self.base_url}/discover/movie?api_key={self.api_key}&language={self.language}&with_genres={genre_id}&page=1"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['results']
        else:
            return []

    def get_movie_details(self, movie_id):
        url = f"{self.base_url}/movie/{movie_id}?api_key={self.api_key}&language={self.language}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else {}

    def get_movie_credits(self, movie_id):
        url = f"{self.base_url}/movie/{movie_id}/credits?api_key={self.api_key}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else {}
