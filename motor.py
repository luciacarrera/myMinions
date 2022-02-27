import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import pybullet as p


class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName
        #self.Prepare_To_Act()


    def Set_Value(self, robotId, desiredAngle):
        self.amplitude = c.amplitude
        self.offset = c.phaseOffset
        self.frequency = c.frequency # do we remove these???

        self.posJoint = self.amplitude * numpy.sin(self.frequency * desiredAngle + self.offset)
        values01 = numpy.linspace(c.startingValue, c.stoppingValue, c.ITERATIONS)
        self.values =  numpy.sin(values01)

        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = c.force)
   
