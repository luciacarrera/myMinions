from simulation import SIMULATION

print("aqui")
simulation = SIMULATION()
print("aqui 2")

simulation.Run
print("PART·")
'''
import numpy as numpy
import random
import constants as c

robotId = p.loadURDF("body.urdf")


# numpy vector to store sensor values
backLegSensorValues = numpy.zeros(c.ITERATIONS)
frontLegSensorValues = numpy.zeros(c.ITERATIONS)

# sin stuff
targetValues01 = numpy.linspace(c.startingValue, c.stoppingValue, c.ITERATIONS)
targetValues =  numpy.sin(targetValues01)
numpy.save('data/targetValues.npy',targetValues)

p.disconnect()

'''