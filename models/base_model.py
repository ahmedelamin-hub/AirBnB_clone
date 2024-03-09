#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.
        
        Args:
            *args (any): Unused.
            **kwargs (dict): Key-value pairs of attributes.
        """
        if kwargs:
            # Process each key-value pair in kwargs.
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    # Convert string to datetime object.
                    value = datetime.fromisoformat(value)
                # Set attribute for the instance.
                setattr(self, key, value)
        else:
            # If kwargs is empty, set default attributes.
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
    
    def __str__(self):
        """Returns the string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        # Convert datetime objects to strings in ISO format.
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
