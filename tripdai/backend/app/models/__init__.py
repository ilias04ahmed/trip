from sqlalchemy import (
    Column, Integer, String, Text, Numeric, DateTime, ForeignKey, JSON, DECIMAL, TIME
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)

    profile = relationship('Profile', back_populates='user', uselist=False)
    preferences = relationship('Preference', back_populates='user')
    itineraries = relationship('Itinerary', back_populates='user')


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    traveler_type = Column(String(50))
    budget = Column(Numeric(10,2))
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)

    user = relationship('User', back_populates='profile')


class Preference(Base):
    __tablename__ = 'preferences'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    interests = Column(JSON)            # e.g. ["cultura","aventura"]
    duration_days = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)

    user = relationship('User', back_populates='preferences')
    itineraries = relationship('Itinerary', back_populates='preferences')


class Destination(Base):
    __tablename__ = 'destinations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100))
    description = Column(Text)
    latitude = Column(DECIMAL(9,6))
    longitude = Column(DECIMAL(9,6))
    popularity = Column(Integer, default=0)

    activities = relationship('Activity', back_populates='destination')


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True, index=True)
    destination_id = Column(Integer, ForeignKey('destinations.id', ondelete='CASCADE'))
    name = Column(String(150), nullable=False)
    type = Column(String(50))           # comida, museo, outdoor
    cost_estimate = Column(Numeric(10,2))
    location = Column(String(255))
    tags = Column(JSON)                 # ["gastronomía","historia"]
    avg_duration_minutes = Column(Integer)

    destination = relationship('Destination', back_populates='activities')
    itinerary_items = relationship('ItineraryItem', back_populates='activity')


class Itinerary(Base):
    __tablename__ = 'itineraries'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    preferences_id = Column(Integer, ForeignKey('preferences.id', ondelete='SET NULL'))
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)

    user = relationship('User', back_populates='itineraries')
    preferences = relationship('Preference', back_populates='itineraries')
    items = relationship('ItineraryItem', back_populates='itinerary')


class ItineraryItem(Base):
    __tablename__ = 'itinerary_items'
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey('itineraries.id', ondelete='CASCADE'))
    day_order = Column(Integer)
    activity_id = Column(Integer, ForeignKey('activities.id'))
    start_time = Column(TIME)
    end_time = Column(TIME)

    itinerary = relationship('Itinerary', back_populates='items')
    activity = relationship('Activity', back_populates='itinerary_items')
