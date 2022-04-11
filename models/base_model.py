#!/usr/bin/python3
"""
This module defines the class BaseModel.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    This class defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        This is initialization of the base instance with args and kwargs.
        """
        mod = '%Y-%m-%dT%H:%M:%S.%f'
        if len(args) == 0 and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        date_time_str = datetime.strptime(value, mod)
                        setattr(self, key, date_time_str)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        THis method return a readable string format of an instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        This method updates the public instance attribute 'updated_at' with
        the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This method returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
