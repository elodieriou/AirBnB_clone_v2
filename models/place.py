#!/usr/bin/python3
"""
This module defines the class Place.
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


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
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """"""
            my_list = []
            all_review = models.storage.all('Review')
            for key, value in all_review.items():
                if value.place_id == self.id:
                    my_list.append(value)
            return my_list

        @property
        def amenities(self):
            """"""
            my_list = []
            all_amenity = models.storage.all('Amenity')
            for key, value in all_amenity.items():
                if value.id == self.amenity_ids:
                    my_list.append(value)
            return my_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == 'Amenity':
                self.amenity_ids.append(value.id)
