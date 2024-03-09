#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Represents a file storage."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {obj: self.__objects[obj].to_dict() for obj in self.__objects.keys()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj in obj_dict.values():
                cls_name = obj['__class__']
                self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
