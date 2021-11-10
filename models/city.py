#!/usr/bin/python3
"""Subclass City that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Subclass amenity that inherits from BaseModel
    Args:
        BaseModel (superclass): Defines all common
        attributes/methods for other classes
    Description:
       state_id
       name
    """
    state_id = ""
    name = ""
