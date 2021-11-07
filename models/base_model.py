#!/usr/bin/python3
"""
Class base
"""
from datetime import datetime
import models
import uuid

ftim = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """initialization of the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], ftim)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], ftim)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """update the current date"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns the contents of the dict"""
        dic_t = self.__dict__.copy()
        dic_t["__class__"] = self.__class__.__name__
        dic_t["created_at"] = self.created_at.isoformat()
        dic_t["updated_at"] = self.updated_at.isoformat()
        return dic_t
