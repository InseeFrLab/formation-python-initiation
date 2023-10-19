import requests
import pandas
import seaborn as sns
import matplotlib.pyplot as plt


def build_request_nominatim(country, city):
    url_request = f"https://nominatim.openstreetmap.org/search?country={country}&city={city}&format=json"
    return url_request


def get_lat_long(country, city):
    url_request = build_request_nominatim(country, city)
    response = requests.get(url_request)
    code = response.status_code
    if code == 200:
        json_data = response.json()
        latitude = float(json_data[0]["lat"])
        longitude = float(json_data[0]["lon"])
        return latitude, longitude
    else:
        print(f"Erreur lors de la récupération des données météo. Code d'erreur : {code}")
        return None


def get_meteo_data(latitude, longitude):
    url_request = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=relativehumidity_2m,windspeed_10m"
    response = requests.get(url_request)
    code = response.status_code
    if code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la récupération des données météo. Code d'erreur : {code}")
        return None
