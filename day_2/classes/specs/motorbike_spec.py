import unittest
import sys

sys.path.append(".")
sys.path.append("..")

from motorbike import *

class TestMotorbike(unittest.TestCase):

    def setUp(self):
        self.motorbike = Motorbike(2, "Yamaha", 950)

    def test_motorbike_can_start_engine(self):
        self.assertEqual("Vrrmmm (I'm a motorbike)", self.motorbike.start_engine())

    def test_motorbike_has_number_of_wheels(self):
        self.assertEqual(2, self.motorbike.number_of_wheels)

    def test_motorbike_has_make(self):
        self.assertEqual("Yamaha", self.motorbike.model)

    def test_motorbike_has_engine_size(self):
        self.assertEqual(950, self.motorbike.engine_size)

if __name__ == "__main__":
    unittest.main()
