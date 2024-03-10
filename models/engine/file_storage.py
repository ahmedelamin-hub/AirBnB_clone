#!/usr/bin/python3
"""
FileStorage class serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.
        If a cls is specified, returns a dictionary of models of type cls.
        """
        if cls:
            cls_name = cls if type(cls) == str else cls.__name__
            return {k: v for k, v in self.__objects.items() if v.__class__.__name__ == cls_name}
        return FileStorage.__objects

    def new(self, obj):
        """Adds the object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {obj: self.__objects[obj].to_dict() for obj in self.__objects.keys()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if __file_path exists."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj in obj_dict.items():
                cls_name = obj['__class__']
                cls = globals()[cls_name]
                self.__objects[obj_id] = cls(**obj)
        except FileNotFoundError:
            pass
