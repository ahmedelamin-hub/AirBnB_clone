#!/usr/bin/python3
"""
Defines a BaseModel class.
This class will be the base for all other classes in our project.
It includes common attributes and methods that can be inherited.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Defines the BaseModel class.
    Attributes:
        id (str): unique id for each instance.
        created_at (datetime): the current datetime when an instance is created.
        updated_at (datetime): the current datetime when an instance is created and
                               it will be updated every time the instance is changed.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        If kwargs is not empty, it initializes the instance attributes accordingly,
        converting datetime strings back to datetime objects.
        Otherwise, it creates a new instance with unique id and current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        This dictionary also contains the class name under the key '__class__'.
        The datetime attributes are converted to strings in ISO format.
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
