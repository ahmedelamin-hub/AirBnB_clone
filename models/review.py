#!/usr/bin/python3
"""
Defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review for the AirBnB clone.
    Attributes:
        place_id (str): The Place.id the review is for.
        user_id (str): The User.id of the reviewer.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
