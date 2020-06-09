from vehicle import *

class Motorbike(Vehicle):

    def __init__(self, number_of_wheels, model, engine_size):
        Vehicle.__init__(self, number_of_wheels)
        self.model = model
        self.engine_size = engine_size

    def start_engine(self):
        return Vehicle.start_engine(self) + " (I'm a motorbike)"
