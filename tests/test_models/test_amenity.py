#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
from models import amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test the Amenity class
    """
    def setUp(self):
        """
        Set up an instance of Amenity
        """
        self.amenity = amenity.Amenity()

    def test_init(self):
        """
        Test if object is an instance of Amenity and BaseModel
        """
        self.assertIsInstance(self.amenity, amenity.Amenity)
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertEqual(self.amenity.name, "")

    def test_attr_types(self):
        """
        Test the attributes of Amenity
        """
        self.assertEqual(type(self.amenity.name), str)

    def test_inheritance(self):
        """
        Test if Amenity is a subclass of BaseModel
        """
        # Test if Amenity is a subclass of BaseModel
        self.assertTrue(issubclass(amenity.Amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
