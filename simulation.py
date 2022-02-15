import pybullet_data
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time as t
import numpy as numpy
import random

PI = numpy.pi
ITERATIONS = 1000

amplitudeFL = -PI/4
amplitudeBL = +PI/4
frequencyFL = 1/10
frequencyBL = 1/20
phaseOffsetFL = 5
phaseOffsetBL = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-50)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

# prepares sensors
pyrosim.Prepare_To_Simulate(robotId)

# numpy vector to store sensor values
backLegSensorValues = numpy.zeros(ITERATIONS)
frontLegSensorValues = numpy.zeros(ITERATIONS)

# sin stuff
targetValues01 = numpy.linspace(-PI/4.0, PI/4.0, ITERATIONS)
targetValues =  numpy.sin(targetValues01)
numpy.save('data/targetValues.npy',targetValues)

for i in range(0,ITERATIONS):
    t.sleep(1/60.0)
    p.stepSimulation()

    # sin stuff
    posBackLeg = amplitudeFL * numpy.sin(frequencyFL * i + phaseOffsetFL)
    posFrontLeg = amplitudeBL * numpy.sin(frequencyBL * i + phaseOffsetBL)

    # creates sensor for backleg        
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    numpy.save('data/backLegSensorValues.npy',backLegSensorValues)

    # creates a sensor for frontleg
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    numpy.save('data/frontLegSensorValues.npy',frontLegSensorValues)

    # motor backleg
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = posBackLeg, maxForce = 50)
    
    # motor frontleg
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition= posFrontLeg, maxForce = 50)


p.disconnect()

