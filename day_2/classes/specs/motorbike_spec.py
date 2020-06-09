import unittest
import sys

sys.path.append(".")
sys.path.append("..")

from motorbike import *

class TestMotorbike(unittest.TestCase):

  def setUp(self):
    self.motorbike = Motorbike()

  def test_motorbike_can_start_engine(self):
    self.assertEqual("Vrrmmm", self.motorbike.start_engine())

if __name__ == "__main__":
    unittest.main()
