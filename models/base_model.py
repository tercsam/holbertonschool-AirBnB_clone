#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class with common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (str): Unique identifier.
            created_at (datetime): Creation datetime.
            updated_at (datetime): Last update datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of BaseModel instance.

        Returns:
            str: String representation in the format '[<class name>] (<self.id>) <self.__dict__>'
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
