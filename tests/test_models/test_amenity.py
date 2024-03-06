#!/usr/bin/python3

"""
Module with unittests for Amenity class.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test class for Amenity class.
    """

    def test_1_create_amenity(self):
        """
        Test if name is initialized to an empty string.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_2_set_amenity_name(self):
        """
        Test setting the name attribute of an Amenity instance.
        """
        amenity = Amenity()
        amenity.name = "Batsignal"
        self.assertEqual(amenity.name, "Batsignal")

    def test_3_amenity_instance_of_base_model(self):
        """
        Test if an Amenity instance is also an instance of BaseModel.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)


if __name__ == "__main__":
    unittest.main()
