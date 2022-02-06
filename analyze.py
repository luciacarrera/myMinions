import numpy as numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
plt.plot(backLegSensorValues)
plt.show()
