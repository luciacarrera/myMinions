import numpy as numpy
import matplotlib.pyplot as plt


backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
plt.plot(backLegSensorValues, label = "Backleg", linewidth = 3)

frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
plt.plot(frontLegSensorValues, label = "Frontleg", linewidth = 1)
plt.legend()
plt.show()
