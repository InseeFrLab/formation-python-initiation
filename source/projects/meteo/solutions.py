import requests
import pandas
import seaborn as sns
import matplotlib.pyplot as plt


def build_request_nominatim(country, city):
    url_request = f"https://nominatim.openstreetmap.org/search?country={country}&city={city}&format=json"
    return url_request


def get_lat_long(query):
    response = requests.get(query)
    code = response.status_code
    if code == 200:
        json_data = response.json()
        latitude = float(json_data[0]["lat"])
        longitude = float(json_data[0]["lon"])
        return latitude, longitude
    else:
        print(f"Erreur lors de la récupération des données météo. Code d'erreur : {code}")
        return None


def build_request_open_meteo(latitude, longitude):
    url_request = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=relativehumidity_2m,windspeed_10m"
    return url_request


def get_meteo_data(query):
    response = requests.get(query)
    code = response.status_code
    if code == 200:
        data = response.json()
        return data
    else:
        print(f"Erreur lors de la récupération des données météo. Code d'erreur : {code}")
        return None
