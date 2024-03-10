#!/usr/bin/python3
"""
FileStorage class serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json
import models

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds obj to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects if __file_path exists"""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for obj_id, obj_data in objs.items():
                cls_name = obj_data['__class__']
                cls = getattr(models, cls_name, None)
                if cls:
                    self.__objects[obj_id] = cls(**obj_data)
        except FileNotFoundError:
            pass
