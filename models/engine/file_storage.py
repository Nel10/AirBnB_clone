#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances
"""
from json import load, dump, dumps
from models.base_model import BaseModel
from os.path import exists

classes_name = ["BaseModel": BaseModel]

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_json_object = {}
        for key in self.__objects:
            dict_json_object[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dict_json_object, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        dict_obje = {}
        self.__objects = {}
        if (exists(self.__file_path)):
            with open(self.__file_path, 'r') as f:
                dict_obje = load(f)
                for key, value in dict_obje.items():
                    class_n = key.split(".")[0]
                    if class_n in classes_name:
                        self.__objects[key] = eval(class_n)
                    else:
                        pass
