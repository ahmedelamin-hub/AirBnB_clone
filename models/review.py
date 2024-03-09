#!/usr/bin/python3
"""Defines the Review class."""

from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review for a HBNB project."""
    place_id = ""  # Will be the Place.id
    user_id = ""  # Will be the User.id
    text = ""
