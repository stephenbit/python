import unittest
import sys

sys.path.append(".")
sys.path.append("..")

from vehicle import *

class TestVehicle(unittest.TestCase):

  def setUp(self):
    self.vehicle = Vehicle(4)

  def test_vehicle_can_start_engine(self):
    self.assertEqual("Vrrmmm", self.vehicle.start_engine())

if __name__ == "__main__":
    unittest.main()
