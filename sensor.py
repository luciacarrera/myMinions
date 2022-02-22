import constants as c
import numpy as numpy


class SENSOR:

    def __init__(self, linkname):

        self.linkname = linkname
        # numpy vector to store sensor values
        self.values = numpy.zeros(c.ITERATIONS)
