from app import app
from flask import redirect, render_template, session, request
from app.controllers.movie_controller import MovieController
from app.controllers.user_controller import user_blueprint

# Instanciar el controlador de películas
movie_controller = MovieController()

# Registrar el blueprint de usuarios
@app.after_request
def no_cache(response):
    # Verificar si la ruta actual es la página de login o registro
    if request.endpoint in ['users.render_login_form', 'users.render_register_form', 'page_not_found']:
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response

# Manejo de errores 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('general/error.html'), 404

# Ruta principal de las peliculas
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect('/users/login')  
    return redirect('/movies')  

# Ruta para la página de películas
@app.route('/movies', endpoint='movie.index')
def movie_index():
    if 'user_id' not in session:
        return redirect('/users/login')  
    return movie_controller.index() 

# Ruta para los detalles de la película
@app.route('/movie/<int:movie_id>', methods=['GET'], endpoint='movie.show')
def show(movie_id):
    if 'user_id' not in session:
        return redirect('/users/login')  
    return movie_controller.show(movie_id)

# Ruta para la búsqueda de películas
@app.route('/search')
def search():
    if 'user_id' not in session:
        return redirect('/users/login')  
    return movie_controller.search()
