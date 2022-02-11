import pybullet_data
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time as t
import numpy as numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

# prepares sensors
pyrosim.Prepare_To_Simulate(robotId)

# numpy vector to store sensor values
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

for i in range(0,101):
    t.sleep(1/60)
    p.stepSimulation()
    
    # creates sensor for backleg
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    numpy.save('data/backLegSensorValues.npy',backLegSensorValues)

    
    # creates a sensor for frontleg
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    numpy.save('data/frontLegSensorValues.npy',frontLegSensorValues)

    # motors
    

    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = ...,

    maxForce = ...)


p.disconnect()

