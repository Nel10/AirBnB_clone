#!/usr/bin/python3
"""
Class base
"""

from datetime import datetime
import models
import uuid
ft_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """initialization of the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, ft_dt)
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """update the current date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns the contents of the dict"""
        dic_t = {}
        for key, item in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dic_t[key] = item

        dic_t['__class__'] = self.__class__.__name__
        dic_t['created_at'] = self.created_at.isoformat()
        dic_t['updated_at'] = self.updated_at.isoformat()
        return dic_t
