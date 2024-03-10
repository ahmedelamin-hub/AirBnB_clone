#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Defines test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test case."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Tear down the test case."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test that new() properly adds objects to the storage."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that save() properly saves objects to file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as f:
            obj_dict = json.load(f)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, obj_dict)

    def test_reload(self):
        """Test that reload() properly loads objects from file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
