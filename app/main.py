# app/main.py
from flask import Flask
from app.controllers.movie_controller import MovieController

app = Flask(__name__)

# Instanciar el controlador
movie_controller = MovieController()

@app.route('/')
def index():
    return movie_controller.index()

if __name__ == '__main__':
    app.run(debug=True)
