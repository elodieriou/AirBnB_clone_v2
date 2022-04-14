#!/usr/bin/python3
"""
This module contains unit tests for tha database storage.
"""

from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime
from os import getenv
import MySQLdb
import unittest
import models
import json
import uuid
import os


class TestDBStorage(unittest.TestCase):
    """This class setup and tear down for test"""

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "skip file storage")
    def setUp(self):
        if getenv("HBNB_TYPE_STORAGE") == "db":
            host = getenv("HBNB_MYSQL_HOST")
            user = getenv("HBNB_MYSQL_USER")
            pwd = getenv("HBNB_MYSQL_PWD")
            db = getenv("HBNB_MYSQL_DB")
            self.connection = MySQLdb.connect(host, user, pwd, db)
            self.cursor = self.connection.cursor()

    def tearDown(self):
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.connection.close()


class TestClassAttributes(unittest.TestCase):
    """This class provides tests with attributes of the class DBStorage"""

    def test_class_attribute_engine(self):
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))

    def test_class_attribute_session(self):
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))


class TestNew(unittest.TestCase):
    """This class provides tests for new() method"""

    def test_new_state(self):
        new_state = State()
        new_state.name = "California"
        models.storage.new(new_state)
        models.storage.save()
        self.assertEqual("California", new_state.name)


class TestAll(unittest.TestCase):
    """This class provides tests for all() method"""

    def test_all_state_type(self):
        all_state = models.storage.all(State)
        self.assertEqual(type(all_state), dict)


if __name__ == "__main__":
    unittest.main()
