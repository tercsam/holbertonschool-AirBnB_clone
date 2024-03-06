#!/usr/bin/python3

"""
Module with unittests for State class.
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test class for State class.
    """

    def test_1_create_state(self):
        """
        Test if name is initialized to an empty string.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_2_set_state_name(self):
        """
        Test setting the name attribute of a State instance.
        """
        state = State()
        state.name = "Toulouse"
        self.assertEqual(state.name, "Toulouse")

    def test_3_state_instance_of_base_model(self):
        """
        Test if a State instance is also an instance of BaseModel.
        """
        state = State()
        self.assertIsInstance(state, BaseModel)


if __name__ == "__main__":
    unittest.main()
