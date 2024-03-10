#!/usr/bin/python3
"""
Defines the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city for the AirBnB clone.
    Attributes:
        state_id (str): The State.id the city is in.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
