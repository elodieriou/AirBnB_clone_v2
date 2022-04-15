#!/usr/bin/python3
"""
This module defines the class Amenity.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    This class defines the amenity.
    Attribute:
        - name (str)
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary=place_amenity)
