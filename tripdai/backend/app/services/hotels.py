# Cliente para la API de Booking/Expedia
import os
import requests

API_KEY = os.getenv("BOOKING_API_KEY")
BASE_URL = "https://api.booking.com/v1"

def search_hotels(location: str, checkin: str, checkout: str):
    params = {
        "apikey": API_KEY,
        "location": location,
        "checkin_date": checkin,
        "checkout_date": checkout
    }
    r = requests.get(f"{BASE_URL}/hotels", params=params)
    return r.json()
