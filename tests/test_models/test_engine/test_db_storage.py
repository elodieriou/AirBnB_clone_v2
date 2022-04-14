#!/usr/bin/python3
"""
This module contains unit tests for tha database storage.
"""
import unittest
import pycodestyle
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """This class provides tests for the database storage"""

    def test_conformance(self):
        """Test that we conform to pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertEqual(len(DBStorage.__doc__), 59)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertGreater(len(DBStorage.all.__doc__), 0)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertLess(len(DBStorage.save.__doc__), 100)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertEqual(len(DBStorage.reload.__doc__), 51)


if __name__ == "__main__":
    unittest.main()
