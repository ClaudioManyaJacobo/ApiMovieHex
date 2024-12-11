import requests

API_KEY = "e5d86b492f30d1b695069fefdfe9abd0"
BASE_URL = "https://api.themoviedb.org/3"

# Buscar la película "Moana" en español latinoamericano
search_url = f"{BASE_URL}/search/movie"
search_params = {
    "api_key": API_KEY,
    "query": "Moana",
    "language": "es-MX"
}

search_response = requests.get(search_url, params=search_params)

if search_response.status_code == 200:
    search_results = search_response.json().get("results", [])
    if search_results:
        # Obtener el ID de la película más relevante
        movie_id = search_results[0]["id"]
        
        # Obtener detalles de la película incluyendo el póster
        details_url = f"{BASE_URL}/movie/{movie_id}"
        details_params = {
            "api_key": API_KEY,
            "language": "es-MX"
        }
        
        details_response = requests.get(details_url, params=details_params)
        
        if details_response.status_code == 200:
            movie_details = details_response.json()
            poster_path = movie_details.get("poster_path")
            
            if poster_path:
                poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            else:
                poster_url = "https://via.placeholder.com/500x750?text=No+Image"
            
            print(f"Póster de 'Moana' (Latino): {poster_url}")
        else:
            print("Error al obtener los detalles de la película:", details_response.status_code)
    else:
        print("No se encontraron resultados para 'Moana'.")
else:
    print("Error al realizar la búsqueda:", search_response.status_code)
