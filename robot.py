import os
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy as numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:

    def __init__(self, solutionID):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.swarmIds = []
        for i in range(0, c.swarm):
            bodyFile = "body"+ str(i)+".urdf"
            self.swarmIds.append(p.loadURDF(bodyFile))
        
        for Id in self.swarmIds:
            pyrosim.Prepare_To_Simulate(Id)
        
        self.Prepare_To_Sense()

        self.Prepare_To_Act()

        self.solutionID = str(solutionID)

        # creates a neural netrwork
        nnFile = "brain" + solutionID + ".nndf"
        self.nn = NEURAL_NETWORK(nnFile)
        os.system("del " + nnFile)
        

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

                for Id in self.swarmIds:
                    self.motors[jointName].Set_Value(Id, desiredAngle)
                #print(neuronName,jointName,desiredAngle)


    def Think(self):
        self.nn.Update()
        #self.nn.Print()
    
    def Get_Fitness(self):
        # get total X position
        totalX = 0
        # get best X pos
        bestX = 100
        for Id in self.swarmIds:
            basePositionAndOrientation = p.getBasePositionAndOrientation(Id)
            basePosition = basePositionAndOrientation[0]
            xPosition = basePosition[0]
            totalX += xPosition

            # get best X considering best fitness is the smallest
            if xPosition < bestX:
                bestX = xPosition
        
        # get average xPos
        averageX = totalX / c.swarm

        # write coordinate in file
        tmpFileName = "temp" + self.solutionID + ".txt"
        fitnessFileName = "fitness" + self.solutionID + ".txt"
        fitnessFile = open(tmpFileName, "w")
        fitnessFile.write(str(averageX))
        fitnessFile.close()

        print("\n\n")
        command = "rename " + tmpFileName + " " + fitnessFileName
        #print(command)

        os.system(command)
