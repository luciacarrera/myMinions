import constants as c
import numpy as numpy
import pyrosim.pyrosim as pyrosim


class SENSOR:

    def __init__(self, linkName):

        self.linkName = linkName
        # numpy vector to store sensor values
        self.values = numpy.zeros(c.ITERATIONS)

    def Get_Value(self, t):
        # file = 'data/'+self.linkname+'.npy'
        # numpy.save(file,self.values)
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # if t == c.ITERATIONS -1:
        #    print(self.values)

