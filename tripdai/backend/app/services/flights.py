# Cliente para la API de Skyscanner
import os
import requests

API_KEY = os.getenv("SKYSCANNER_API_KEY")
BASE_URL = "https://partners.api.skyscanner.net/apiservices"

def search_flights(origin: str, destination: str, date: str):
    params = {
        "apiKey": API_KEY,
        "country": "ES",
        "currency": "EUR",
        "locale": "es-ES",
        "originPlace": origin,
        "destinationPlace": destination,
        "outboundDate": date
    }
    r = requests.get(f"{BASE_URL}/browseroutes/v1.0/ES/EUR/es-ES/{origin}/{destination}/{date}", params=params)
    return r.json()
