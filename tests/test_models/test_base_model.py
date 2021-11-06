#!/usr/bin/python3
"""Test BaseModel"""
import unittest
import os
from models.base_model import BaseModel
import pep8


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
