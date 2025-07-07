import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"

def get_current_weather(lat: float, lon: float):
    params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric", "lang": "es"}
    r = requests.get(f"{BASE_URL}/weather", params=params)
    data = r.json()
    return {
        "description": data["weather"][0]["description"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"]
    }
