from flask import Flask
from app.controllers.movie_controller import MovieController
from app.controllers.user_controller import user_blueprint
import re

# Crear la aplicación Flask
app = Flask(__name__)
app.secret_key = 'mysecretkey'  # Asegúrate de usar una clave secreta adecuada
app.register_blueprint(user_blueprint, url_prefix='/users')

# Instanciar el controlador de películas
movie_controller = MovieController()

# Filtro para formatear números
@app.template_filter('format_number')
def format_number(value):
    return "{:,}".format(value)

# Importar las rutas y blueprints
from app import routes  # Asegúrate de que este archivo importe todas las rutas necesarias

