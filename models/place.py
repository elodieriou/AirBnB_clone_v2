#!/usr/bin/python3
"""
This module defines the class Place.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """
    This class defines a place.
    Attributes:
        - city_id (str)
        - user_id (str)
        - name (str)
        - description (str)
        - number_rooms (int)
        - number_bathrooms (int)
        - max_guest (int)
        - price_by_night (int)
        - latitude (float)
        - longitude (float)
        - amenity_ids (list(str))
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True, default="")
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
