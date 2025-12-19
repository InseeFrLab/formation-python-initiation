import polars as pl
import requests
from plotnine import ggplot, aes, geom_line, theme_matplotlib, labs

# import solutions
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
        print(f"Error code : {code}")
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
        print(f"Error code : {code}")
        return None

# %%
def preprocess_predictions(predictions):

    df = (
        pl.DataFrame(predictions)
            .select('hourly')
            .unnest('hourly')
            .explode('time', 'relativehumidity_2m', 'windspeed_10m')
            .cast({'time': pl.Datetime})
            .rename({'time': 'date_time', 'relativehumidity_2m': 'humidity', 'windspeed_10m': 'wind_speed'})
            .with_columns(
                day=pl.col('date_time').dt.date(), 
                hour=pl.col('date_time').dt.hour(), 
                bad_hair_index=pl.col.humidity*pl.col.wind_speed
            )
    )

    return df

# %%
def plot_agg_avg_bhi(df_preds, agg_var="day"):
    plot = (
        ggplot(df_preds.group_by(agg_var).agg(pl.mean('bad_hair_index')), aes(x=agg_var, y='bad_hair_index'))
            + geom_line()
            + theme_matplotlib()
    )
    if agg_var == "day":
        plot = (
            plot
            + labs(
                title="Evolution of the average BHI on 7 days",
                x='Hour', 
                y='Average Bad Hair Index')
        )
    elif agg_var == "hour":
        plot = (
            plot
            + labs(
                title="Average BHI by hour on the next 7 days",
                x='Day',
                y='Average Bad Hair Index')
        )
    
    return plot


# %%
def main(country, city, agg_var="day"):
# def main(agg_var="day"):
    # Get lat, long from Nominatim API
    url_request_nominatim = build_request_nominatim(country, city)
    lat, long = get_lat_long(query=url_request_nominatim)
    # lat, long = (48.8188544, 2.3194375)

    # Get wheather predictions
    url_request_open_meteo = build_request_open_meteo(latitude=lat, longitude=long)
    predictions = get_meteo_data(url_request_open_meteo)
    df_preds = preprocess_predictions(predictions)

    # Graphical representation
    return plot_agg_avg_bhi(df_preds, agg_var)

# %%
main('France', 'Montrouge', 'day')

# %%
main('France', 'Montrouge', 'hour')