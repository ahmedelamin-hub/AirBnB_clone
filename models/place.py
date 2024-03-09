#!/usr/bin/python3
"""Defines the Place class."""

from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place for a HBNB project."""
    city_id = ""  # Will be the City.id
    user_id = ""  # Will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # Will be the list of Amenity.id
