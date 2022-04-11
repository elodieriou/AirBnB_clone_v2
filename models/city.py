#!/usr/bin/python3
"""
This module defines the class City.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class define a city.
    Attributes:
        - state_id (str)
        - name (str)
    """
    state_id = ""
    name = ""
