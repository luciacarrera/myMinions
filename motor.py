import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import pybullet as p


class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName
        self.Prepare_To_Act()

    
    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.offset = c.phaseOffset

        if self.jointName == "Torso_Frontleg":
            self.frequency = -c.frequency/2
            print("\nTORSO")
        else:
            self.frequency = c.frequency



    def Set_Value(self, robotId, t):

        self.posJoint = self.amplitude * numpy.sin(self.frequency * t + self.offset)
        values01 = numpy.linspace(c.startingValue, c.stoppingValue, c.ITERATIONS)
        self.values =  numpy.sin(values01)

        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.values[t], maxForce = c.force)
   
    def Save_Values(self):
            file = 'data/'+self.jointName+'.npy'
            numpy.save(file,self.values)