#!/usr/bin/python3
"""Contains the FileStorage class models"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

     def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        cls_name = cls.__name__
        dct = {}
        for key in self.__objects.keys():
            if key.split('.')[0] == cls_name:
                dct[key] = self.__objects[key]
        return dct

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to JSON file"""
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
             with open(self.__file_path, encoding="utf-8") as f:
                 for obj in json.load(f).values():
                     self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """ deletes the object obj from the attribute
            __objects if it's inside it
        """
        if obj is None:
            return
        obj_key = obj.to_dict()['__class__'] + '.' + obj.id
        if obj_key in self.__objects.keys():
            del self.__objects[obj_key]
