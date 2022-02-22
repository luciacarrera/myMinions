import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
from sensor import SENSOR
from motor import MOTOR
import numpy as numpy

class ROBOT:

    def __init__(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.Id = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.Id)

        self.Prepare_To_Sense()

        self.Prepare_To_Act()
        

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for jointName in self.motors:
            self.motors[jointName].Set_Value(self.Id, t) 


