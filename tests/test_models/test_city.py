#!/usr/bin/python3

"""
Module with unittests for City class.
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test class for City class.
    """

    def test_1_create_city(self):
        """
        Test if state_id and name are initialized to empty strings.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_2_set_city_attributes(self):
        """
        Test setting the attributes of a City instance.
        """
        city = City()
        city.state_id = "31000"
        city.name = "Toulouse"

        self.assertEqual(city.state_id, "31000")
        self.assertEqual(city.name, "Toulouse")

    def test_3_city_instance_of_base_model(self):
        """
        Test if a City instance is also an instance of BaseModel.
        """
        city = City()
        self.assertIsInstance(city, BaseModel)


if __name__ == "__main__":
    unittest.main()
