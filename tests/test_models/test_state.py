#!/usr/bin/python3
"""
Unit tests for the State class.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Defines test cases for the State class."""

    def setUp(self):
        """Set up method for State tests."""
        self.state = State()

    def tearDown(self):
        """Tear down method for State tests."""
        del self.state

    def test_instance(self):
        """Test if the object is an instance of State."""
        self.assertIsInstance(self.state, State)

    def test_inheritance(self):
        """Test if State is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.state), State))

    def test_attributes(self):
        """Test if State has the correct attributes."""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")


if __name__ == '__main__':
    unittest.main()
