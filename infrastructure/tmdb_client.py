# infrastructure/tmdb_client.py
import requests
from app.config.config import Config

class TMDBClient:
    def __init__(self):
        # Inicializar los valores de configuración (API Key, URL base, idioma y sesión)
        self.api_key = Config.API_KEY
        self.base_url = Config.BASE_URL
        self.language = Config.LANGUAGE
        self.session = requests.Session()  # Usar una sesión persistente para las peticiones HTTP

    # Realiza una solicitud GET a la API de TMDB.
    def _get(self, endpoint, params=None):

        url = f"{self.base_url}/{endpoint}"  # Construir la URL completa
        params = params or {}  # Si no se pasan parámetros, usar un diccionario vacío
        params.update({
            'api_key': self.api_key,  # Incluir la API Key
            'language': self.language  # Incluir el idioma
        })
        
        response = self.session.get(url, params=params)  # Realizar la solicitud GET
        if response.status_code == 200:  # Si la solicitud es exitosa (código 200)
            return response.json()  # Retornar la respuesta en formato JSON
        print(f"Error {response.status_code}: {url}")  # En caso de error, imprimir el código de error y la URL
        return {}  # Retornar un diccionario vacío si hubo un error

    # Obtiene una lista de películas generales desde la API de TMDB.
    def general_movies(self, page=5, max_movies=20):

        movies = []  # Lista para almacenar las películas obtenidas
        seen_ids = set()  # Conjunto para asegurarse de no obtener películas duplicadas
        
        while len(movies) < max_movies:  # Mientras no hayamos obtenido el número máximo de películas
            data = self._get('discover/movie', {'page': page})  # Obtener las películas de la página actual
            for movie in data.get('results', []):  # Iterar sobre las películas en los resultados
                if movie['id'] not in seen_ids:  # Si la película no se ha agregado aún
                    movies.append(self._map_movie_data(movie))  # Mapear los datos de la película y agregarla a la lista
                    seen_ids.add(movie['id'])  # Marcar la película como vista (para no agregarla otra vez)
                if len(movies) >= max_movies:  # Si hemos alcanzado el número máximo de películas
                    break
            if data.get('page') < data.get('total_pages'):  # Si hay más páginas de resultados
                page += 1  # Pasar a la siguiente página
            else:
                break  # Si no hay más páginas, terminar el ciclo
        return movies  # Retornar la lista de películas obtenidas

    # Obtiene los detalles de una película específica.
    def get_movie_details(self, movie_id):
        return self._get(f"movie/{movie_id}")  # Llamar al endpoint correspondiente para obtener los detalles de la película

    # Busca películas basadas en una consulta de texto.
    def search_movies(self, query):
        return self._get('search/movie', {'query': query}).get('results', [])  # Retornar los resultados de la búsqueda

    # Mapea los datos de una película a un formato personalizado.
    def _map_movie_data(self, movie_data):
        actors_director = self.credits_movie(movie_data.get('id'))  # Obtener actores y director de la película
        movie = {
            'title': movie_data.get('title', ''),  # Título de la película
            'overview': movie_data.get('overview', ''),  # Descripción de la película
            'release_date': movie_data.get('release_date', ''),  # Fecha de estreno
            'poster_path': f"https://image.tmdb.org/t/p/w500{movie_data.get('poster_path', '')}",  # URL del poster de la película
            'backdrop_path': f"https://image.tmdb.org/t/p/w1280{movie_data.get('backdrop_path', '')}",  # URL del backdrop de la película
            'genres': [genre['name'] for genre in movie_data.get('genres', [])],  # Lista de géneros de la película
            'actors': actors_director['actors'],  # Obtener los actores de la película
            'director': actors_director['director'],   # Obtener los actores de la película
            'id': movie_data.get('id'),  # ID de la película
            'video_url': self.get_video_url(movie_data.get('id')),  # Obtener la URL del video (trailer)
            'runtime': movie_data.get('runtime', 0),  # Duración de la película en minutos
            'rating': movie_data.get('vote_average', 0),  # Calificación promedio de la película
            'budget': movie_data.get('budget', 0),  # Presupuesto de la película
            'revenue': movie_data.get('revenue', 0),  # Ingresos de la película
            'original_language': movie_data.get('original_language', ''),  # Idioma original de la película
        }
        return movie
     
    # Obtiene los actores y el director de una película.
    def credits_movie(self, movie_id):
        url = f"{self.base_url}/movie/{movie_id}/credits?api_key={self.api_key}&language={self.language}"
        response = self.session.get(url)
        actors = []
        director = 'Unknown Director'

        if response.status_code == 200:
            data = response.json()
            
            for member in data.get('crew', []):
                if member.get('job') == 'Director':
                    director = member.get('name')
                    break  

            actors = [{
                'name': actor['name'],
                'photo': f"https://image.tmdb.org/t/p/w500{actor['profile_path']}" if actor.get('profile_path') else None,
                'profile_url': f"https://www.themoviedb.org/person/{actor['id']}"
            } for actor in data.get('cast', [])][:9] 

        else:
            print(f"Error al obtener actores y director para la película {movie_id}: {response.status_code}")
        
        return {
            'director': director,
            'actors': actors
        }

    # Obtiene la URL del video (trailer) de una película.
    def get_video_url(self, movie_id):
        
        url = f"{self.base_url}/movie/{movie_id}/videos?api_key={self.api_key}&language={self.language}"
        response = self.session.get(url)  # Realizar la solicitud GET para obtener los videos de la película
        
        if response.status_code == 200:  # Si la solicitud es exitosa (código 200)
            video_results = response.json().get('results', [])  # Obtener los resultados de videos
            if video_results:  # Si hay resultados de videos
                # Obtener el primer trailer y devolver la URL
                return f"https://www.youtube.com/watch?v={video_results[0]['key']}"
        return ''