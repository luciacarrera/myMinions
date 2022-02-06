import numpy as numpy
import matplotlib.pyplot as plt


backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
plt.plot(backLegSensorValues)

frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
plt.plot(frontLegSensorValues)
plt.show()
