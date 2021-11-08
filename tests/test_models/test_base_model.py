#!/usr/bin/python3
"""Test BaseModel"""
import unittest
import datetime
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """Test BaseModel"""

    def setUp(self):
        """set up"""
        self.basemodel = BaseModel()

    def test_pep8(self):
        """test for check pep8"""
        style = pep8.StyleGuide(quiet=True)
        syntax = style.check_files(['models/base_model.py'])
        self.assertEqual(syntax.total_errors, 0, "check pep8")

    def test_docstring(self):
        """check module docstring"""
        self.assertTrue(len(self.basemodel.__doc__) > 0)

    def test_created_at(self):
        """test created_at"""
        BaseModel_to_dict = self.basemodel.to_dict()
        model = BaseModel(BaseModel_to_dict)
        self.assertTrue(isinstance(model.created_at, datetime.datetime))

    def test_updated_at(self):
        """test updated_at"""
        BaseModel_to_dict = self.basemodel.to_dict()
        model = BaseModel(BaseModel_to_dict)
        self.assertTrue(isinstance(model.updated_at, datetime.datetime))

    def test_id(self):
        """checks id"""
        self.assertEqual("<class 'str'>", str(type(self.basemodel.id)))

    def test_save(self):
        """test save"""
        updated = self.basemodel.updated_at
        self.basemodel.save()
        updated2 = self.basemodel.updated_at
        self.assertNotEqual(updated, updated2)

    def test_args(self):
        """check for args"""
        ele = BaseModel("element")
        self.assertNotIn("element", ele.__dict__.values())

    def test_kwargs(self):
        """check for kwargs"""
        self.basemodel.name = "Holberton"
        self.basemodel.my_number = 89
        json_attr = self.basemodel.to_dict()
        basemodel2 = BaseModel(**json_attr)
        self.assertIsInstance(basemodel2, BaseModel)
        self.assertIsInstance(json_attr, dict)
        self.assertIsNot(self.basemodel, basemodel2)

    def test_json_file(self):
        """check file json"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        self.basemodel.save()
        key = "BaseModel." + self.basemodel.id
        with open("file.json", 'r') as f:
            json = f.read()
        self.assertTrue(key in json)

    def test_is_an_instance(self):
        """check if is an instance"""
        self.assertIsInstance(self.basemodel, BaseModel)

    def test_check_id(self):
        """check id are different"""
        basemodel2 = BaseModel()
        self.assertNotEqual(self.basemodel.id, basemodel2.id)

    def test_dict_clss(self):
        """check class"""
        self.assertEqual("BaseModel", (self.basemodel.to_dict())["__class__"])
