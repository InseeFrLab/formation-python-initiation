import polars as pl
import requests
import seaborn as sns
import matplotlib.pyplot as plt

# import solutions

def build_request_nominatim(country, city):
    url_request = f"https://nominatim.openstreetmap.org/search?country={country}&city={city}&format=json"
    return url_request

requests.get(build_request_nominatim('France', 'Montrouge'))

def get_lat_long(query):
    response = requests.get(query)
    code = response.status_code
    if code == 200:
        json_data = response.json()
        latitude = float(json_data[0]["lat"])
        longitude = float(json_data[0]["lon"])
        return latitude, longitude
    else:
        print(f"Error code : {code}")
        return None


def build_request_open_meteo(latitude, longitude):
    url_request = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=relativehumidity_2m,windspeed_10m"
    return url_request


response_json = requests.get(build_request_open_meteo(48.8188544, 2.3194375)).json()
pl.DataFrame(response_json).select('hourly').unnest('hourly')
pl.DataFrame(response_json).unnest('hourly')
(
    pl.DataFrame(response_json)\
        .select('hourly')
        .unnest('hourly')
        .explode('time', 'relativehumidity_2m', 'windspeed_10m')
        .cast({'time':pl.Datetime})
        .rename({'time': 'date_time', 'relativehumidity_2m': 'humidity', 'windspeed_10m': 'wind_speed'})
        .with_columns(
            date=pl.col('date_time').dt.date(), 
            time=pl.col('date_time').dt.time(), 
            bhi=pl.col.humidity*pl.col.wind_speed
        )
)