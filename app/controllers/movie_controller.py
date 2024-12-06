# application/controllers/movie_controller.py
from flask import render_template, request
from app.services.movie_service import MovieService
from infrastructure.tmdb_movie_repository import TMDBMovieRepository

# Clase para controlar las peticiones relacionadas con las películas
class MovieController:
    def __init__(self):
        # Inicializamos el servicio de películas con el repositorio de películas de TMDB
        movie_repository = TMDBMovieRepository() 
        self.movie_service = MovieService(movie_repository)

    # Metodo para mostrar todas las películas (index)
    def index(self):
        movies = self.movie_service.get_movies()
        return render_template('movies.html', movies=movies)

    # Metodo para mostrar los detalles de una película (show)
    def show(self, movie_id):
        movie = self.movie_service.get_movie_details(movie_id)
        return render_template('show.html', movie=movie)

    # Metodo para buscar películas (search)
    def search(self):
        query = request.args.get('query')
        movies = []
        if query:
            movies = self.movie_service.search_movies(query)
        return render_template('movies.html', movies=movies, query=query)
