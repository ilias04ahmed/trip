from pydantic import BaseModel, EmailStr, condecimal
from typing import List, Optional
from datetime import datetime, time

# Usuarios
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# Perfil
class ProfileCreate(BaseModel):
    traveler_type: str
    budget: condecimal(max_digits=10, decimal_places=2)

class ProfileOut(ProfileCreate):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Preferencias
class PreferenceCreate(BaseModel):
    interests: List[str]
    duration_days: int

class PreferenceOut(PreferenceCreate):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Destinos y Actividades
class ActivityOut(BaseModel):
    id: int
    name: str
    type: str
    cost_estimate: condecimal(max_digits=10, decimal_places=2)
    location: str
    tags: List[str]
    avg_duration_minutes: int

    class Config:
        orm_mode = True

class DestinationOut(BaseModel):
    id: int
    name: str
    country: Optional[str]
    description: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    popularity: int
    activities: List[ActivityOut] = []

    class Config:
        orm_mode = True

# Itinerarios
class ItineraryItemOut(BaseModel):
    id: int
    day_order: int
    activity: ActivityOut
    start_time: time
    end_time: time

    class Config:
        orm_mode = True

class ItineraryOut(BaseModel):
    id: int
    user_id: int
    preferences_id: Optional[int]
    created_at: datetime
    items: List[ItineraryItemOut] = []

    class Config:
        orm_mode = True

class ItineraryCreateRequest(BaseModel):
    user_id: int
    preferences_id: int

class ItineraryGenerateResponse(BaseModel):
    itinerary_id: int
