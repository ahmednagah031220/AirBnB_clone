#!/usr/bin/python3
"""Base Model for AirBnB project console"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """BaseModel class instances with methods"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()
        if kwargs:
            dictionary_mod = self.__dict__
            for item, result in kwargs.items():
                if item == "created_at" or item == "updated_at":
                    value = datetime.strptime(kwargs[item],
                                              "%Y-%m-%dT%H:%M:%S.%f")
                    dictionary_mod[item] = value
                else:
                    dictionary_mod[item] = result
        else:
            models.storage.new(self)

    def to_dict(self):
        """returns dict contains variables and class name"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    def save(self):
        """Save the file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """returns string defining class"""
        re_value = "[{}] ({}) {}".format(self.__class__.__name__,
                                         self.id,
                                         dict(self.__dict__))
        return re_value
