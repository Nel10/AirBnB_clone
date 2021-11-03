#!/usr/bin/python3
"""Class base"""

from datetime import datetime
from uuid import uuid4
import models
import uuid
import json
format_datetime = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """"""
    def __init__(self, *args, **kwargs):
        """"""
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, format_datetime)
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """"""
        dic_t = {}
        for key, item in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dic_t[key] = item

        dic_t['__class__'] = self.__class__.__name__
        dic_t['created_at'] = self.created_at.isoformat()
        dic_t['updated_at'] = self.updated_at.isoformat()
        return dic_t
