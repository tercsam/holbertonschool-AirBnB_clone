#!/usr/bin/python3
"""Module for File Storage unittests."""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test the functionality of the FileStorage class
    """
    def setUp(self):
        """Set up the tests"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.maxDiff = None

    def test_objects(self):
        """Test __objects"""
        file_storage = FileStorage()
        self.assertIsInstance(file_storage._FileStorage__objects, dict)

    def test_all(self):
        """
        Test the all method of the FileStorage class
        """        
        self.assertEqual(type(self.storage.all()), dict)
        self.storage.new(self.model)
        self.assertEqual(
            self.storage.all(),
            self.storage._FileStorage__objects
        )

    def test_new(self):
        """
        Test the new method of the FileStorage class
        """
        self.storage.new(self.model)
        key = self.model.__class__.__name__ + "." + self.model.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """
        Test the save method of the FileStorage class
        """
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

        with open('file.json', 'r') as file:
            self.assertIn("BaseModel." + self.model.id, json.load(file))

    def test_model_save(self):
        """
        Test the save method of the BaseModel class
        """
        old_updated_at = self.model.updated_at
        self.storage.new(self.model)
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_reload(self):
        """Test reload()"""
        self.assertTrue(os.path.exists("file.json"))
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        with open("file.json", 'r') as file:
            self.assertIn("BaseModel." + self.model.id, json.load(file))

        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertNotEqual(self.storage.all(), {})


if __name__ == "__main__":
    unittest.main()
