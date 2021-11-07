#!/usr/bin/python3
"""Test BaseModel"""
import unittest
import datetime
from models.base_model import BaseModel
import pep8 as pycodestyle


class TestBaseModel(unittest.TestCase):
    """Test BaseModel"""

    def setUp(self):
        """set up"""
        self.basemodel = BaseModel()

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
