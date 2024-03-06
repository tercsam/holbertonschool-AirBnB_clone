#!/usr/bin/python3

"""
Module with unittests for Place class.
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test class for Place class.
    """

    def test_1_create_place(self):
        """
        Test if all attributes are initialized to their default values.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_2_set_place_attributes(self):
        """
        Test setting the attributes of a Place instance.
        """
        place = Place()
        place.city_id = "31000"
        place.user_id = "007"
        place.name = "Wayne Manor"
        place.description = "I'm Batman."
        place.number_rooms = 42
        place.number_bathrooms = 7
        place.max_guest = 22
        place.price_by_night = 1000000
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["1", "2", "3"]

        self.assertEqual(place.city_id, "31000")
        self.assertEqual(place.user_id, "007")
        self.assertEqual(place.name, "Wayne Manor")
        self.assertEqual(place.description, "I'm Batman.")
        self.assertEqual(place.number_rooms, 42)
        self.assertEqual(place.number_bathrooms, 7)
        self.assertEqual(place.max_guest, 22)
        self.assertEqual(place.price_by_night, 1000000)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["1", "2", "3"])

    def test_3_place_instance_of_base_model(self):
        """
        Test if a Place instance is also an instance of BaseModel.
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)


if __name__ == "__main__":
    unittest.main()
