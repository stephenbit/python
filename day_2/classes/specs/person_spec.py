import unittest
import sys

sys.path.append(".")
sys.path.append("..")

from person import *

class PersonTest(unittest.TestCase):

    def setUp(self):
        person1 = Person("Barry", 35)

    def test_person_has_name(self):
        self.assertEqual(person1.name, "Barry")
