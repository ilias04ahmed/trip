from sqlalchemy.orm import Session
from app.models import (
    User, Profile, Preference,
    Destination, Activity,
    Itinerary, ItineraryItem
)
from app.schemas import (
    UserCreate, PreferenceCreate,
    ItineraryCreateRequest
)
from typing import List

# Usuarios
def create_user(db: Session, user_in: UserCreate):
    user = User(email=user_in.email, password_hash=hash_password(user_in.password))
    db.add(user); db.commit(); db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Preferencias
def create_preference(db: Session, user_id: int, prefs: PreferenceCreate):
    pref = Preference(user_id=user_id, interests=prefs.interests, duration_days=prefs.duration_days)
    db.add(pref); db.commit(); db.refresh(pref)
    return pref

def get_preferences(db: Session, user_id: int):
    return db.query(Preference).filter(Preference.user_id == user_id).all()

# Destinos
def list_destinations(db: Session) -> List[Destination]:
    return db.query(Destination).order_by(Destination.popularity.desc()).all()

def get_activities_for_destination(db: Session, dest_id: int) -> List[Activity]:
    return db.query(Activity).filter(Activity.destination_id == dest_id).all()

# Itinerarios
def create_itinerary(db: Session, req: ItineraryCreateRequest):
    itin = Itinerary(user_id=req.user_id, preferences_id=req.preferences_id)
    db.add(itin); db.commit(); db.refresh(itin)
    return itin

def add_item_to_itinerary(db: Session, itinerary_id: int, activity_id: int, day: int, start, end):
    item = ItineraryItem(
        itinerary_id=itinerary_id,
        activity_id=activity_id,
        day_order=day,
        start_time=start,
        end_time=end
    )
    db.add(item); db.commit(); db.refresh(item)
    return item

def get_itinerary(db: Session, itinerary_id: int):
    return db.query(Itinerary).filter(Itinerary.id == itinerary_id).first()
