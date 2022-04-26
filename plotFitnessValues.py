import numpy as numpy
import matplotlib.pyplot as plt

# get values
valuesA = numpy.load("data/avFit_A.npy")
valuesB = numpy.load("data/avFit_B.npy")

# get rows of matrix (A and B will have same shape)
rows = valuesA.shape[0]
cols = valuesA.shape[1]

x = []
for i in range(0, cols):
    x.append(i)


for i in range(0, rows):
    labelA = "Variant A, P" + str(i)
    labelB = "Variant B, P" + str(i)
    plt.plot(x, valuesA[i,:], label = labelA, linewidth = 1)
    plt.plot(x, valuesB[i,:], label = labelB, linewidth = 3)

plt.legend()
plt.show()

'''

plt.plot(valuesA[0,:])
plt.show()
plt.plot(valuesB[0,:])
plt.show()

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
plt.plot(backLegSensorValues, label = "Variant A", linewidth = 3)

frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
plt.plot(frontLegSensorValues, label = "Variant B", linewidth = 1)
plt.legend()
plt.show()

'''