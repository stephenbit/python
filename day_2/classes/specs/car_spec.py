import unittest
import sys

sys.path.append(".")
sys.path.append("..")

from car import *

class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_car_can_start_engine(self):
        self.assertEqual("Vrrmmm", self.car.start_engine())

if __name__ == "__main__":
    unittest.main()
