from fastapi import FastAPI
from app.routers import auth, preferences, itineraries, destinations

app = FastAPI(title="TripdAI API")

app.include_router(auth.router, prefix="/api/auth")
app.include_router(preferences.router, prefix="/api/preferences")
app.include_router(itineraries.router, prefix="/api/itineraries")
app.include_router(destinations.router, prefix="/api/destinations")
