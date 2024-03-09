#!/usr/bin/python3
"""recreate a BaseModel from another one"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes and deserialize instances to a JSON file"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects with key <obj class name>.id."""

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects if the JSON file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj_data in obj_dict.items():
                class_name = obj_data['__class__']
                del obj_data['__class__']
                obj = BaseModel(**obj_data) if class_name == 'BaseModel' else None
                if obj:
                    FileStorage.__objects[obj_id] = obj
        except FileNotFoundError:
            pass

