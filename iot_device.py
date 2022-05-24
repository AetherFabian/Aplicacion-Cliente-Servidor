from random import randint
import psutil

# Class definition
class Sensor:

    # Class contructor
    def __init__(self):
        self._sensor = psutil.sensors_temperatures()

    def get_temp(self):
        return self._sensor['coretemp']

    # temps simulations
    def get_random_number(self):
        return randint(0, 100)
