import requests

API_KEY = "e5d86b492f30d1b695069fefdfe9abd0"
MOVIE_ID = 550  # Cambia este ID por el de la película que buscas.

url = f"https://api.themoviedb.org/3/movie/{MOVIE_ID}/credits"
params = {"api_key": API_KEY}
response = requests.get(url, params=params)

if response.status_code == 200:
    credits = response.json()
    cast = credits.get("cast", [])
    
    for actor in cast:
        name = actor.get("name")
        profile_path = actor.get("profile_path")
        if profile_path:
            profile_url = f"https://image.tmdb.org/t/p/w500{profile_path}"
        else:
            profile_url = "https://via.placeholder.com/500x750?text=No+Image"
        
        print(f"Actor: {name}, Foto: {profile_url}")
else:
    print("Error al obtener los créditos:", response.status_code)
