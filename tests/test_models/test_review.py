#!/usr/bin/python3

"""
Module with unittests for Review class.
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test class for Review class.
    """

    def test_1_create_review(self):
        """
        Test if place_id, user_id, and text are initialized to empty strings.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_2_set_review_attributes(self):
        """
        Test setting the attributes of a Review instance.
        """
        review = Review()
        review.place_id = "31000"
        review.user_id = "007"
        review.text = "I'm Batman."

        self.assertEqual(review.place_id, "31000")
        self.assertEqual(review.user_id, "007")
        self.assertEqual(review.text, "I'm Batman.")

    def test_3_review_instance_of_base_model(self):
        """
        Test if a Review instance is also an instance of BaseModel.
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)


if __name__ == "__main__":
    unittest.main()
