#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Defines test cases for the Amenity class."""

    def setUp(self):
        """Set up each test case."""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down each test case."""
        del self.amenity

    def test_instance(self):
        """Test if the object is an instance of Amenity."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_inheritance(self):
        """Test if Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.amenity), Amenity))

    def test_attributes(self):
        """Test if Amenity has the correct attributes."""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_id(self):
        """Test if id is assigned correctly."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_save(self):
        """Test if the save method updates `updated_at`."""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_to_dict(self):
        """Test if to_dict method creates a dictionary with proper keys."""
        self.amenity.name = "Pool"
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["name"], "Pool")
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertTrue("created_at" in amenity_dict)
        self.assertTrue("updated_at" in amenity_dict)
        self.assertTrue("id" in amenity_dict)


if __name__ == '__main__':
    unittest.main()
