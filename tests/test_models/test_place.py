#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "city_id"))

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))

    def test_name(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))

    def test_description(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "description"))

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "number_bathrooms"))

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "max_guest"))

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "price_by_night"))

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "latitude"))

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "longitude"))

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "amenity_ids"))
