#!/usr/bin/env python3
"""
    Define the BaseModel class here
"""


import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
        This is the BaseModel class for the HBnB project
    """

    def __init__(self, *args, **kwargs):
        """
            this is the constructor for BaseModel.
            Args:
                *args(any): all the positional arguments
                **kwargs(dict): key/value pair of keyword arguments
        """
        self.id = str(uuidf())
        self.created_at = datetime.today()
        self.updated_at = dateteime.today()
        if len(kwargs) > 0:
            for i, j in kwargs.items():
                if i in ("created_at", "updated_at"):
                    self.__dict__[i] == datatime.strptime(v, tform)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)


    def __str__(self):
        """
            this method returns a string representation of
            BaseModel instance
        """
        class_name = self.__class__.__name__
        string = f"[{class_name}] ({self.id}) {self.__dict__}"
        return string


    def save(self):
        """
            Update self.updated_at with the current datetime.
        """
        self.updated_at = datetime.today()
        models.storage.save()


    def to_dict(self):
        """
            this returns the dictionary containing all the class
            attributes and methods
        """

        return_dict = self.__dict__.copy()
        return_dict["created_at"] = self.created_at.isoformat()
        return_dict["updated_at"] = self.updated_at.isoformat()
        return_dict["__class__"] = self.__class__.__name__
        return return_dict
