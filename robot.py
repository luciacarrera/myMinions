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

        # array for swarm's neural network
        self.nnFiles = []

        # creates a neural netrwork
        # for the entire swarm
        for i in range(0, c.swarm):
            nnFile = "brain_b" + str(i) + "v" +solutionID + ".nndf"
            self.nnFiles.append(NEURAL_NETWORK(nnFile))
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
        robId = 0
        for nn in self.nnFiles:
            for neuronName in nn.Get_Neuron_Names():
                if nn.Is_Motor_Neuron(neuronName):
                    jointName = nn.Get_Motor_Neurons_Joint(neuronName)
                    desiredAngle = nn.Get_Value_Of(neuronName)

                    
                    self.motors[jointName].Set_Value(robId, desiredAngle)
            robId += 1
                    #print(neuronName,jointName,desiredAngle)


    def Think(self):
        for nn in self.nnFiles:
            nn.Update()
            #nn.Print()
    
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
