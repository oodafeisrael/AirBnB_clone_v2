#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        filtered_dic = {}
        if cls is None:
            return self.__objects
        else:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    filtered_dic[key] = self.__objects[key]
            return (filtered_dic)

    def delete(self, obj=None):
        """Removes an object from the storage dictionary"""
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects.update({obj.to_dict()['__class__'] +
                              '.' + obj.id: obj}))

    def save(self):
        """serialize the file path to JSON file path"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = self.model_classes
        try:
            with open(self.__file_path, 'r',
                       encoding="UTF-8") as f:
                for key, val in (json.load(f)).items():
                    value = eval(val["__class__"])(**val)
                    self.__objects[key] = val)
        except FileNotFoundError:
            pass

    def close(self):
        """Closes the storage engine."""
        self.reload()
