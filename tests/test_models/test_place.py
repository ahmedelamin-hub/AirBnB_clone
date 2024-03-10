#!/usr/bin/python3
"""
Unit tests for the Place class.
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Defines test cases for the Place class."""

    def setUp(self):
        """Set up method for Place tests."""
        self.place = Place()

    def tearDown(self):
        """Tear down method for Place tests."""
        del self.place

    def test_instance(self):
        """Test if the object is an instance of Place."""
        self.assertIsInstance(self.place, Place)

    def test_inheritance(self):
        """Test if Place is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.place), Place))

    def test_attributes(self):
        """Test if Place has the correct attributes."""
        attrs = ["city_id", "user_id", "name", "description", "number_rooms",
                 "number_bathrooms", "max_guest", "price_by_night", "latitude",
                 "longitude", "amenity_ids"]
        for attr in attrs:
            self.assertTrue(hasattr(self.place, attr))
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
