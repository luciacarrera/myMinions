import time
import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import constants as c

class SOLUTION:

    def __init__(self, myID):
        self.ROWS = 3
        self.COLUMNS = 2
        self.weights =  numpy.random.rand(self.ROWS,self.COLUMNS)
        self.weights = self.weights * 2 - 1
        #self.myID = str(myID)

    def Start_Simulation(self,directOrGui):
        self.Create_World()
        self.Generate_Brain()
        self.Generate_Body()
        os.system("start /B python3 simulate.py " + directOrGui + " " + self.myID)
        

    def Wait_For_Simulation_To_End(self):
        # read fitness
        fitnessFileName = "fitness" + self.myID + ".txt"

        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        fitnessFile = open(fitnessFileName, "r")
        self.fitness = float(fitnessFile.readline())
        #print(self.fitness)
        fitnessFile.close()
        os.system("del "+ fitnessFileName)
        #self.GET_FITNESS()

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
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
 
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")

        # generate synapses
        # iterate over sensor neurons
        for currentRow in range(0, c.numSensorNeurons):
            # iterate over motor neurons
            for currentColumn in range(0,c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,weight = self.weights[currentRow][currentColumn])
                 
        pyrosim.End()

    def Mutate(self):
        chosenRow = random.randint(0,self.ROWS - 1)
        chosenColumn = random.randint(0,self.COLUMNS - 1)
        self.weights[chosenRow, chosenColumn] = random.random() * c.numMotorNeurons - 1 #might need to change 2 for numMotorNeurons

    def SET_ID(self, myID):
        self.myID = str(myID)

    def GET_FITNESS(self):
        print("\n-------------FITNESS: ",self.fitness,"\n")