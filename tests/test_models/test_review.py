#!/usr/bin/python3
"""
Unit tests for the Review class.
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Defines test cases for the Review class."""

    def setUp(self):
        """Set up method for Review tests."""
        self.review = Review()

    def tearDown(self):
        """Tear down method for Review tests."""
        del self.review

    def test_instance(self):
        """Test if the object is an instance of Review."""
        self.assertIsInstance(self.review, Review)

    def test_inheritance(self):
        """Test if Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.review), Review))

    def test_attributes(self):
        """Test if Review has the correct attributes."""
        attrs = ["place_id", "user_id", "text"]
        for attr in attrs:
            self.assertTrue(hasattr(self.review, attr))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == '__main__':
    unittest.main()
