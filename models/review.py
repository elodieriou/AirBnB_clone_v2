#!/usr/bin/python3
"""
This module defines the class Review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines a review.
    Attributes:
        - place_id (str)
        - user_id (str)
        - text (str)
    """
    place_id = ""
    user_id = ""
    text = ""
