from random import randint
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import pybullet as p
import pybullet_data


class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName
        self.Prepare_To_Act()

    
    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBL
        self.frequency = c.frequencyBL
        self.offset = c.phaseOffsetBL


    def Set_Value(self, robotId, t):

        self.posJoint = self.amplitude * numpy.sin(self.frequency * t + self.offset)
        motorValues01 = numpy.linspace(c.startingValue, c.stoppingValue, c.ITERATIONS)
        self.motorValues =  numpy.sin(motorValues01)
        
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[t], maxForce = c.force)
