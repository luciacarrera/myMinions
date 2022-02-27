import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
from sensor import SENSOR
from motor import MOTOR
import numpy as numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:

    def __init__(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.Id = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.Id)

        self.Prepare_To_Sense()

        self.Prepare_To_Act()

        # creates a neural netrwork
        self.nn = NEURAL_NETWORK("brain.nndf")
        

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.Id, desiredAngle)
                print(neuronName,jointName,desiredAngle)


        #for jointName in self.motors:
        #   self.motors[jointName].Set_Value(self.Id, t) 

    def Think(self):
        self.nn.Update()
        self.nn.Print()
