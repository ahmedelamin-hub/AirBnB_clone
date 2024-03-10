#!/usr/bin/python3
"""function for storage engine"""
from models.base_model import BaseModel
import json

class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
            from models.base_model import BaseModel  # Import here to avoid circular import
            for key, value in objects.items():
                cls_name = value['__class__']
                if cls_name == "BaseModel":
                    self.new(BaseModel(**value))
        except FileNotFoundError:
            pass
