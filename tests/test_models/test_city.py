#!/usr/bin/python3
"""
Unit tests for the City class.
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Defines test cases for the City class."""

    def setUp(self):
        """Set up each test case."""
        self.city = City()

    def tearDown(self):
        """Tear down each test case."""
        del self.city

    def test_instance(self):
        """Test if the object is an instance of City."""
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """Test if City is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.city), City))

    def test_attributes(self):
        """Test if City has the correct attributes."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_id(self):
        """Test if id is assigned correctly."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_save(self):
        """Test if the save method updates `updated_at`."""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_to_dict(self):
        """Test if to_dict method creates a dictionary keys."""
        self.city.name = "San Francisco"
        self.city.state_id = "CA1234"
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["name"], "San Francisco")
        self.assertEqual(city_dict["state_id"], "CA1234")
        self.assertEqual(city_dict["__class__"], "City")
        self.assertTrue("created_at" in city_dict)
        self.assertTrue("updated_at" in city_dict)
        self.assertTrue("id" in city_dict)


if __name__ == '__main__':
    unittest.main()
