import unittest
import sys

sys.path.append(".")
sys.path.append("..")

from person import *

class PersonTest(unittest.TestCase):

    def setUp(self):
        self.person1 = Person("Barry", 35)

    def test_person_has_name(self):
        self.assertEqual(self.person1.name(), "Barry")

    def test_this_person_can_talk(self):
        self.assertEqual(self.person1.talk(), "Hi, my name is Barry and I am 35 years old")

    def test_can_set_name(self):
        self.person1.set_name("Ally")
        self.assertEqual(self.person1.name(), "Ally")

if __name__ == "__main__":
    unittest.main()
