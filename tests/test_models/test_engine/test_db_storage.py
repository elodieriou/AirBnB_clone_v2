#!/usr/bin/python3
"""
This module contains unit tests for tha database storage.
"""
import unittest
import pycodestyle


class TestDBStorage(unittest.TestCase):
    """This class provides tests for the database storage"""

    def test_conformance(self):
        """Test that we conform to pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
