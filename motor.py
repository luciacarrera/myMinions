import pyrosim.pyrosim as pyrosim
import constants as c
import numpy


class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName
        self.Prepare_To_Act()

    
    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBL
        self.frequency = c.frequencyBL
        self.offset = c.phaseOffsetBL

        self.posJoint = self.amplitude * numpy.sin(self.frequency * i + self.offset)

        motorValues01 = numpy.linspace(c.startingValue, c.stoppingValue, c.ITERATIONS)
        self.motorValues =  numpy.sin(motorValues01)

        # pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = posBackLeg, maxForce = c.force)
