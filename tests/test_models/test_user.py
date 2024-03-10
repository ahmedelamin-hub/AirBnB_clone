#!/usr/bin/python3
"""
Unit tests for the User class.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Defines test cases for the User class."""

    def setUp(self):
        """Set up method for User tests."""
        self.user = User()

    def tearDown(self):
        """Tear down method for User tests."""
        del self.user

    def test_instance(self):
        """Test if the object is an instance of User."""
        self.assertIsInstance(self.user, User)

    def test_inheritance(self):
        """Test if User is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.user), User))

    def test_attributes(self):
        """Test if User has the correct attributes."""
        attrs = ["email", "password", "first_name", "last_name"]
        for attr in attrs:
            self.assertTrue(hasattr(self.user, attr))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
