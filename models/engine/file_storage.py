#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        dict_json_object = {}
        with open(self.__file_path, 'w') as f:
            if self.__objects is not None:
                for key, valu in self.__objects.items():
                    dict_json_object[key] = valu.to_dict()
            json.dump(dict_json_object, f)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, mode='r') as f:
                for key, valu in (json.load(f)).items():
                    valu = eval(valu["__class__"])(**valu)
                    self.__objects[key] = valu

        except FileNotFoundError:
            pass
