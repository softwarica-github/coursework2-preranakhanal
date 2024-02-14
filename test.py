from addvoter import create_new_voter
import unittest

class TestValidation(unittest.TestCase):
    def test_create_new_voter_valid(self):
        self.assertTrue(create_new_voter("Prerana Khanal", 2003, 75132, 9800000000, "KTM"))

    def test_create_new_voter_invalid(self):
        with self.assertRaises(ValueError):
            create_new_voter("Prerana Khanal", "200", 75132, 9800000000, "KTM")