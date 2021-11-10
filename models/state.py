#!/usr/bin/python3
"""Subclass Review that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Subclass amenity that inherits from BaseModel
    Args:
        BaseModel (superclass): Defines all common
        attributes/methods for other classes
    Description:
        name
    """
    name = ""
