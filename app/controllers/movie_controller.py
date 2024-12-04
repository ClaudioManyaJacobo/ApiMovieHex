# app/controllers/movie_controller.py
from flask import render_template
from app.services.movie_service import MovieService

class MovieController:
    def __init__(self):
        self.movie_service = MovieService()

    def index(self):
        movies = self.movie_service.get_movies()
        return render_template('movies.html', movies=movies)

    def show(self, movie_id):
        movie = self.movie_service.get_movie_details(movie_id)  # Llamada correcta
        return render_template('show.html', movie=movie)
