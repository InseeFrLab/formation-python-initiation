import requests
import pandas as pd
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


def preprocess_predictions(predictions):
    data_dict = {
        'time': predictions['hourly']["time"],
        'humidity': predictions['hourly']["relativehumidity_2m"],
        'wind_speed': predictions['hourly']["windspeed_10m"]
    }
    df = pd.DataFrame(data_dict)

    df['time'] = pd.to_datetime(df['time'])
    df['day'] = df['time'].dt.day
    df['hour'] = df['time'].dt.hour
    df['bad_hair_index'] = df['humidity'] * df['wind_speed']

    return df


def plot_agg_avg_bhi(df_preds, agg_var="day"):
    df_agg = df_preds.groupby(agg_var).agg({'bad_hair_index': 'mean'})
    df_agg = df_agg.reset_index()

    sns.lineplot(x=agg_var, y='bad_hair_index', data=df_agg)
    plt.ylabel('Bad Hair Index moyen')
    if agg_var == "day":
        plt.title("Évolution du Bad Hair Index moyen sur 7 jours")
        plt.xlabel('Jour')
    elif agg_var == "hour":
        plt.title("Moyenne du Bad Hair Index heure par heure sur 7 jours")
        plt.xlabel('Heure')


def main(country, city, agg_var="day"):
    # Récupération de la latitude et longitude via l'API nominatim
    url_request_nominatim = build_request_nominatim(country, city)
    lat, long = get_lat_long(query=url_request_nominatim)

    # Récupération des prédictions météos
    url_request_open_meteo = build_request_open_meteo(latitude=lat, longitude=long)
    predictions = get_meteo_data(url_request_open_meteo)

    # Mise en forme des prédictions
    df_preds = preprocess_predictions(predictions)

    # Représentation graphique selon l'agrégation demandée
    plot_agg_avg_bhi(df_preds, agg_var)
