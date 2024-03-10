#!/usr/bin/python3
"""
Defines class User that inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines the User class that inherits from BaseModel.
    Attributes:
        email (str): user's email address.
        password (str): user's password.
        first_name (str): user's first name.
        last_name (str): user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
