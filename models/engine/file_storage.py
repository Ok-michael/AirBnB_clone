#!/usr/bin/env python3
"""
    We define a class FileStorage here
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
        this represents an abstract storage engine.
        Attributes:
            __file_path(str): the name of the file to save in
            __objects (dict): A dictionary of intantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            returns the dictionary FileStorage.__objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets __objects with key <obj_class_name>.id
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
            Serialize __objects to JSON file __file_path
        """
        obj_dict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
