# app/main.py
from flask import Flask, redirect, render_template
from app.controllers.movie_controller import MovieController
import re
app = Flask(__name__)

# Instanciar el controlador
movie_controller = MovieController()

# Filtro para embeber videos de YouTube, Vimeo y Dailymotion
@app.template_filter('youtube_embed')
def embed_video(url):
    if url:
        # Expresión regular para detectar URLs de YouTube
        youtube_pattern = r'(https?://(?:www\.)?youtube\.com/(?:[^/]+/|(?:.*\?v=|(?:e(?:mbed)?/)?)([\w\-]{11})))|(?:youtu\.be/([\w\-]{11}))'
        # Expresión regular para detectar URLs de Vimeo
        vimeo_pattern = r'(https?://(?:www\.)?vimeo\.com/(\d+))'
        # Expresión regular para detectar URLs de Dailymotion
        dailymotion_pattern = r'(https?://(?:www\.)?dailymotion\.com/video/([^_]+))'
        
        # Verificar si es un enlace de YouTube
        match_youtube = re.search(youtube_pattern, url)
        if match_youtube:
            video_id = match_youtube.group(2) if match_youtube.group(2) else match_youtube.group(3)
            return f"https://www.youtube.com/embed/{video_id}"

        # Verificar si es un enlace de Vimeo
        match_vimeo = re.search(vimeo_pattern, url)
        if match_vimeo:
            video_id = match_vimeo.group(2)
            return f"https://player.vimeo.com/video/{video_id}"

        # Verificar si es un enlace de Dailymotion
        match_dailymotion = re.search(dailymotion_pattern, url)
        if match_dailymotion:
            video_id = match_dailymotion.group(2)
            return f"https://www.dailymotion.com/embed/video/{video_id}"

    return url  

# Filtro para formatear números
@app.template_filter('format_number')
def format_number(value):
    return "{:,}".format(value)

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

if __name__ == '__main__':
    app.run(debug=True)
