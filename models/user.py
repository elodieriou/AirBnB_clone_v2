#!/usr/bin/python3
"""
This module defines the class User.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class defines a user.
    Attributes:
        - email (str)
        - password (str)
        - first_name (str)
        - last_name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
