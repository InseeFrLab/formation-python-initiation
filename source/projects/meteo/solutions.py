import requests
import pandas
import seaborn as sns
import matplotlib.pyplot as plt


def renvoie_lat_long(localisation):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": localisation,
        "format": "json"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        json_data = response.json()
        latitude = float(json_data[0]["lat"])
        longitude = float(json_data[0]["lon"])
        return (latitude, longitude)
    else:
        print(f"Erreur lors de la récupération des coordonnées de {localisation}")
        return None

def fetch_meteo_data(latitude, longitude, start_date, end_date):
    url_request = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=relativehumidity_2m,windspeed_10m"
    response = requests.get(url_request)
    code = response.status_code 
    if code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la récupération des données météo. Code d'erreur : {code}")
        return None

