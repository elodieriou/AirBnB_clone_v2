#!/usr/bin/python3
"""
This module defines the class User.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """
    This class defines a user.
    Attributes:
        - email (str)
        - password (str)
        - first_name (str)
        - last_name (str)
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
