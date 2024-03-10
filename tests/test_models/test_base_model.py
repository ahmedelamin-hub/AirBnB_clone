#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Defines test cases for the BaseModel class."""

    def setUp(self):
        """Set up method for BaseModel tests."""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down method for BaseModel tests."""
        del self.model

    def test_init(self):
        """Test initialization and type of attributes."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test the string representation."""
        string = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), string)

    def test_save(self):
        """Test the save method updates `updated_at`."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for JSON."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

        self.assertTrue('__class__' in model_dict)
        self.assertEqual(model_dict['__class__'], self.model.__class__.__name__)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_init_kwargs(self):
        """Test initialization with kwargs."""
        model = BaseModel(name="Test", number=10)
        self.assertTrue(hasattr(model, 'name') and model.name == "Test")
        self.assertTrue(hasattr(model, 'number') and model.number == 10)


if __name__ == '__main__':
    unittest.main()
