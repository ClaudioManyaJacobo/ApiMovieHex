# app/routes.py
from app import app
from flask import redirect, render_template
from app.controllers.movie_controller import MovieController

movie_controller = MovieController()

# Ruta principal
@app.route('/')
def index():
    return redirect('/welcome')

# Ruta para la pantalla de bienvenida
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  

# Ruta para los detalles de la película
@app.route('/movies')
def movie_index():
    return movie_controller.index()

# Ruta para los detalles de la película
@app.route('/movie/<int:movie_id>', methods=['GET'], endpoint='movie.show')
def show(movie_id):
    return movie_controller.show(movie_id) 

# Ruta para la búsqueda de películas
@app.route('/search')
def search():
    return movie_controller.search() 
