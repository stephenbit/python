import unittest
import sys

sys.path.append(".")
sys.path.append("..")

from car import *

class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car(4, "Ford")

    def test_car_can_start_engine(self):
        self.assertEqual("Vrrmmm", self.car.start_engine())

    def test_car_has_wheels(self):
        self.assertEqual(4, self.car.number_of_wheels)

    def test_car_has_make(self):
        self.assertEqual("Ford", self.car.model)

if __name__ == "__main__":
    unittest.main()
