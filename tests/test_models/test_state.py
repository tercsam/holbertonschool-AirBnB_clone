#!/usr/bin/python3
"""Unittest for State class"""

import unittest
from models import state
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test the State class
    """
    def setUp(self):
        """
        Set up an instance of State
        """
        self.state = state.State()

    def test_init(self):
        """
        Test if object is an instance of State and BaseModel
        """
        self.assertIsInstance(self.state, state.State)
        self.assertIsInstance(self.state, BaseModel)
        self.assertEqual(self.state.name, "")

    def test_attr_types(self):
        """
        Test the attributes of State
        """
        self.assertEqual(type(self.state.name), str)

    def test_inheritance(self):
        """
        Test if State is a subclass of BaseModel
        """
        self.assertTrue(issubclass(state.State, BaseModel))


if __name__ == '__main__':
    unittest.main()
