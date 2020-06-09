from vehicle import *

class Car(Vehicle):

    def __init__(self, number_of_wheels, model):
        Vehicle.__init__(self, number_of_wheels)
        self.model = model
