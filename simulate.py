from simulation import SIMULATION
simulate = SIMULATION()

'''
import constants as c
import pybullet_data
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time as t
import numpy as numpy
import random


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0, c.GRAVITY)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

# prepares sensors
pyrosim.Prepare_To_Simulate(robotId)

# numpy vector to store sensor values
backLegSensorValues = numpy.zeros(c.ITERATIONS)
frontLegSensorValues = numpy.zeros(c.ITERATIONS)

# sin stuff
targetValues01 = numpy.linspace(c.startValue, c.endValue, c.ITERATIONS)
targetValues =  numpy.sin(targetValues01)
numpy.save('data/targetValues.npy',targetValues)

for i in range(0,c.ITERATIONS):
    t.sleep(1/60.0)
    p.stepSimulation()

    # sin stuff
    posBackLeg = c.amplitudeFL * numpy.sin(c.frequencyFL * i + c.phaseOffsetFL)
    posFrontLeg = c.amplitudeBL * numpy.sin(c.frequencyBL * i + c.phaseOffsetBL)

    # creates sensor for backleg        
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    numpy.save('data/backLegSensorValues.npy',backLegSensorValues)

    # creates a sensor for frontleg
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    numpy.save('data/frontLegSensorValues.npy',frontLegSensorValues)

    # motor backleg
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = posBackLeg, maxForce = c.maxForce)
    
    # motor frontleg
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition= posFrontLeg, maxForce = c.maxForce)


p.disconnect()
'''

