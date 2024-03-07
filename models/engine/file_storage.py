#!/usr/bin/python3
"""This module defines the FileStorage class"""

import json
import os


class FileStorage():
    """This class serializes and deserializes 'JSON' files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects."""
        return self.__objects

    def new(self, obj):
        """Set in '__objects' the 'obj' with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialize '__objects' to the 'JSON' file"""

        json_dict = {}

        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        """
        Deserializes the JSON file and restores objects.
        """
        from models import base_model
        from models import user
        from models import state
        from models import city
        from models import amenity
        from models import place
        from models import review

        dict_module = {
            'BaseModel': base_model,
            'User': user,
            'State': state,
            'City': city,
            'Amenity': amenity,
            'Place': place,
            'Review': review
            }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                obj_stored = json.load(file)

            for key, value in obj_stored.items():
                class_name = value["__class__"]

                if class_name in dict_module:
                    model_module = dict_module[class_name]
                    model_class = getattr(model_module, class_name)

                obj_instance = model_class(**value)
                self.__objects[key] = obj_instance
