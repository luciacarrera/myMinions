from simulation import SIMULATION

simulation = SIMULATION()

simulation.Run()

'''
import numpy as numpy
import random
import constants as c



# numpy vector to store sensor values
backLegSensorValues = numpy.zeros(c.ITERATIONS)
frontLegSensorValues = numpy.zeros(c.ITERATIONS)

# sin stuff
targetValues01 = numpy.linspace(c.startingValue, c.stoppingValue, c.ITERATIONS)
targetValues =  numpy.sin(targetValues01)
numpy.save('data/targetValues.npy',targetValues)


'''