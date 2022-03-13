import numpy
import pyrosim.pyrosim as pyrosim
import random
import os


class SOLUTION:

    def __init__(self):
        ROWS = 3
        COLUMNS = 2
        self.weights =  numpy.random.rand(ROWS,COLUMNS)
        self.weights = self.weights * 2 - 1

    def Evaluate(self):
        self.Create_World()
        self.Generate_Brain()
        self.Generate_Body()

        os.system("python3 simulate.py")

        # read fitness
        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.readline())
        fitnessFile.close()
    
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        # cube is part of the world
        length, width, height = 1, 1, 1
        x,y, z = 0,5, height/2
        pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height]  )

        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")

        # LINK: TORSO (abs)
        length, width, height = 1, 1, 1
        x,y, z = 0, 0, 1+height/2
        pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height]  )

        # JOINT: TORSO - Backleg (abs)
        x, y, z = 0.5, 0, 1
        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [x,y,z])
        
        # LINK: Backleg (rel)
        length, width, height = 1, 1, 1
        x,y, z = 0.5,0,-0.5
        pyrosim.Send_Cube(name="Backleg", pos=[x, y, z] , size=[length, width, height]  )
        
        # JOINT: TORSO - Frontleg (abs)
        x, y, z = -0.5, 0, 1
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [x, y, z])

        # LINK: Frontleg (rel)
        length, width, height = 1, 1, 1
        x,y, z = -0.5,0,-0.5
        pyrosim.Send_Cube(name="Frontleg", pos=[x, y, z] , size=[length, width, height]  )
        
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")

        # generate synapses
        # iterate over sensor neurons
        for currentRow in range(0,3):
            # iterate over motor neurons
            for currentColumn in range(0,2):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName=currentColumn + 3,weight = self.weights[currentRow][currentColumn])
                
        pyrosim.End()

