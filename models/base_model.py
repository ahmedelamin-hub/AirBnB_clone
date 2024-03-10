#!/usr/bin/python3
"""
Defines the BaseModel class.
This class is the base for all other classes in the project.
It handles initialization, serialization, and deserialization of instances.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    A base class for other classes to inherit from.
    Attributes:
        id (str): Unique id for each instance.
        created_at (datetime): The current datetime when an instance is created.
        updated_at (datetime): The current datetime when an instance is created and
                               will be updated every time the instance changes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        If kwargs is not empty, initializes the instance attributes accordingly.
        Otherwise, creates a new instance with unique id and current datetime.
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
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime and saves the
        instance to the JSON file.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        This dictionary also contains the class name under the key '__class__'.
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
