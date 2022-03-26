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
        
        ## TORSO
        # LINK: TORSO (abs)
        length, width, height = 1, 1, 1
        x,y, z = 0, 0, 1 # z used to be 1+height/2
        pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height]  )

        ## BACKLEG
        # JOINT: TORSO - Backleg (abs)
        x, y, z = 0, -0.5, 1
        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [x,y,z], jointAxis = "1 0 0")
        # LINK: Backleg (rel)
        length, width, height =  0.2, 1, 0.2
        x, y, z = 0, -0.5, 0
        pyrosim.Send_Cube(name="Backleg", pos=[x, y, z] , size=[length, width, height]  )
        # JOINT: Backleg - LowerBackleg (rel)
        x, y, z = 0, -1, 0
        pyrosim.Send_Joint( name = "Backleg_LowerBackleg" , parent= "Backleg" , child = "LowerBackleg" , type = "revolute", position = [x, y, z], jointAxis = "1 0 0")
        # LINK: LowerBackleg (rel)
        length, width, height = 0.2, 0.2, 1
        x, y, z = 0, 0, -0.5
        pyrosim.Send_Cube(name="LowerBackleg", pos=[x, y, z] , size=[length, width, height]  )
        
        ## FRONTLEG
        # JOINT: TORSO - Frontleg (abs)
        x, y, z = 0, 0.5, 1
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [x, y, z], jointAxis = "1 0 0")
        # LINK: Frontleg (rel)
        length, width, height = 0.2, 1, 0.2
        x, y, z = 0, 0.5, 0
        pyrosim.Send_Cube(name="Frontleg", pos=[x, y, z] , size=[length, width, height]  )
        # LOWER FRONTLEG
        # JOINT: Frontleg - LowerFrontleg (rel)
        x, y, z = 0, 1, 0
        pyrosim.Send_Joint( name = "Frontleg_LowerFrontleg" , parent= "Frontleg" , child = "LowerFrontleg" , type = "revolute", position = [x, y, z], jointAxis = "1 0 0")
        # LINK: LowerFrontleg (rel)
        length, width, height = 0.2, 0.2, 1
        x, y, z = 0, 0, -0.5
        pyrosim.Send_Cube(name="LowerFrontleg", pos=[x, y, z] , size=[length, width, height]  )

        ## LEFTLEG
        # JOINT: TORSO - Leftleg (abs)
        x, y, z = -0.5, 0, 1
        pyrosim.Send_Joint( name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = [x, y, z], jointAxis = "1 0 0")
        # LINK: Leftleg (rel)
        length, width, height = 1, 0.2, 0.2  # SIZE
        x, y, z = -0.5, 0, 0  # POSITION
        pyrosim.Send_Cube(name="Leftleg", pos=[x, y, z] , size=[length, width, height]  )
        # LOWER LEFTLEG
        # JOINT: Leftleg - LowerLeftleg (rel)
        x, y, z = -1, 0, 0
        pyrosim.Send_Joint( name = "Leftleg_LowerLeftleg" , parent= "Leftleg" , child = "LowerLeftleg" , type = "revolute", position = [x, y, z], jointAxis = "1 0 0")
        # LINK: LowerLeftleg (rel)
        length, width, height = 0.2, 0.2, 1
        x, y, z = 0, 0, -0.5
        pyrosim.Send_Cube(name="LowerLeftleg", pos=[x, y, z] , size=[length, width, height]  )
        
        ## RIGHTLEG
        # JOINT: TORSO - RightLeg (abs)
        x, y, z = 0.5, 0, 1
        pyrosim.Send_Joint( name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = [x, y, z], jointAxis = "1 0 0")
        # LINK: RightLeg (rel)
        length, width, height = 1, 0.2, 0.2  # SIZE
        x, y, z = 0.5, 0, 0  # POSITION
        pyrosim.Send_Cube(name="Rightleg", pos=[x, y, z] , size=[length, width, height]  )
         # LOWER RIGHTLEG
        # JOINT: Rightleg - LowerRightleg (rel)
        x, y, z = 1, 0, 0
        pyrosim.Send_Joint( name = "Rightleg_LowerRightleg" , parent= "Rightleg" , child = "LowerRightleg" , type = "revolute", position = [x, y, z], jointAxis = "1 0 0")
        # LINK: LowerRightleg (rel)
        length, width, height = 0.2, 0.2, 1
        x, y, z = 0, 0, -0.5
        pyrosim.Send_Cube(name="LowerRightleg", pos=[x, y, z] , size=[length, width, height]  )

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