# infrastructure/api_service.py
from .tmdb_client import TMDBClient
from domain.movie import Movie

class MovieAPIService:
    def __init__(self):
        self.tmdb_client = TMDBClient()

    def get_movies(self):
        movies_data = self.tmdb_client.get_sci_fi_movies()
        movies = []

        for movie_data in movies_data:
            movie_id = movie_data['id']  # El id de la película
            details = self.tmdb_client.get_movie_details(movie_id)
            credits = self.tmdb_client.get_movie_credits(movie_id)
            videos = self.tmdb_client.get_movie_videos(movie_id)

            genres = [genre['name'] for genre in details.get('genres', [])]
            actors = [actor['name'] for actor in credits.get('cast', [])[:5]]  # Primeros 5 actores
            video_url = None
            if videos:
                # Tomamos el primer video (si existe)
                video_url = f"https://www.youtube.com/watch?v={videos[0]['key']}"

            movie = Movie(
                title=movie_data['title'],
                overview=movie_data['overview'],
                release_date=movie_data['release_date'],
                poster_path=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}",
                genres=genres,
                actors=actors,
                movie_id=movie_id,
                video_url=video_url  # Pasamos la URL del video
            )
            movies.append(movie)

        return movies

    def get_movie_details(self, movie_id):
        details = self.tmdb_client.get_movie_details(movie_id)
        credits = self.tmdb_client.get_movie_credits(movie_id)
        videos = self.tmdb_client.get_movie_videos(movie_id)

        genres = [genre['name'] for genre in details.get('genres', [])]
        actors = [actor['name'] for actor in credits.get('cast', [])[:5]]  # Primeros 5 actores
        video_url = None
        if videos:
            video_url = f"https://www.youtube.com/watch?v={videos[0]['key']}"

        movie = Movie(
            title=details['title'],
            overview=details['overview'],
            release_date=details['release_date'],
            poster_path=f"https://image.tmdb.org/t/p/w500{details['poster_path']}",
            genres=genres,
            actors=actors,
            movie_id=movie_id,
            video_url=video_url  # Pasamos la URL del video
        )
        return movie
