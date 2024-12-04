# app/main.py
from flask import Flask
from app.controllers.movie_controller import MovieController
import re

app = Flask(__name__)

# Instanciar el controlador
movie_controller = MovieController()

@app.template_filter('youtube_embed')
def youtube_embed(url):
    if url:
        # Expresión regular mejorada para detectar URLs de YouTube
        youtube_pattern = r'(https?://(?:www\.)?youtube\.com/(?:[^/]+/|(?:.*\?v=|(?:e(?:mbed)?/)?)([\w\-]{11})))|(?:youtu\.be/([\w\-]{11}))'
        match = re.search(youtube_pattern, url)
        
        if match:
            # Si la URL es larga o corta, obtener el ID del video
            video_id = match.group(2) if match.group(2) else match.group(3)
            return f"https://www.youtube.com/embed/{video_id}"
    
    return url  # Si no es una URL de YouTube, devolver la URL original

@app.route('/')
def index():
    return movie_controller.index()

# Ruta para los detalles de la película
@app.route('/movie/<int:movie_id>', methods=['GET'], endpoint='movie.show')
def show(movie_id):
    return movie_controller.show(movie_id)  

if __name__ == '__main__':
    app.run(debug=True)
