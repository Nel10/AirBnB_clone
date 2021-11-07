#!/usr/bin/python3
"""Test BaseModel"""
import unittest
from datetime import datetime
import models
import pep8 as pycodestyle
BaseModel = models.base_model.BaseModel

class TestBaseModel(unittest.TestCase):
    """Test BaseModel"""

    def setUpClass(self):
        """set up class"""
        self.test_basemodel = BaseModel()

    def test_pep8_BaseModel(self):
        """test with PEP8"""
        pycstyle = pep8.StyleGuide(quiet=True)
        style = pycstyle.check_file(['models/base_model.py'])
        self.assertEqual(style.total_errors, 0, "Check pep8")

    def test_save_BaseModel(self):
        """test save """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_docstring(self):
        """test docstring"""
        self.assertisNotNone(BaseModel.__doc__)

    def test_kwargs(self):
        basemodel = BaseModel(name="base")
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertFalse(hasattr(basemodel, "id"))
        self.assertFalse(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "name"))
        self.assertFalse(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))

if __name__ == "__main__":
    unittest.main()
