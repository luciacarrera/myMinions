from fileinput import filename
import time
import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import constants as c

class SOLUTION:

    def __init__(self, myID):
        self.weights =  numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        #self.myID = str(myID)

    def Start_Simulation(self,directOrGui):
        self.Create_World()

        # generate the individual brain of each robot in the swarm
        for i in range(0, c.swarm):
            self.Generate_Brain(i)

        # I want them to be distributed along the x axis evenly (not starting from 0) and make it look like 
        # a starting line of a race
        distance =( c.swarm -1 ) * c.offset
        position = - distance/2 

        for i in range(0, c.swarm):
            robotNum = i
            self.Generate_Body(position, robotNum)
            position += c.offset
        os.system("start /B python3 simulate.py " + directOrGui + " " + self.myID)
        

    def Wait_For_Simulation_To_End(self):
        # read fitness
        fitnessFileName = "fitness" + self.myID + ".txt"

        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        fitnessFile = open(fitnessFileName, "r")
        self.fitness = float(fitnessFile.readline())
        #exit()
        #print(self.fitness)
        fitnessFile.close()
        os.system("del "+ fitnessFileName)
        #self.GET_FITNESS()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        # cube is part of the world
        length, width, height = 1, 1, 1
        x,y, z = 0,5, height/2
        #pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height]  )

        pyrosim.End()

    def Generate_Body(self, offset, robotNum):
        pyrosim.Start_URDF("body"+ str(robotNum) +".urdf")

        # BASE POSITION
        baseX, baseY, baseZ = 0, offset + 0, 0
        ## TORSO
        # LINK: TORSO (abs)
        length, width, height = 1, 1, 1
        x,y, z = baseX + 0, baseY + 0, baseZ +1 # z used to be 1+height/2
        pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height]  )
        
        ## BACKLEG
        # JOINT: TORSO - Backleg (abs)
        x, y, z = baseX + 0, baseY  -0.5, baseZ +  1
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
        x, y, z = baseX + 0, baseY + 0.5, baseZ +  1
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
        x, y, z = baseX-0.5,baseY +  0, baseZ + 1
        pyrosim.Send_Joint( name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = [x, y, z], jointAxis = "0 1 0")
        # LINK: Leftleg (rel)
        length, width, height = 1, 0.2, 0.2  # SIZE
        x, y, z = -0.5, 0, 0  # POSITION
        pyrosim.Send_Cube(name="Leftleg", pos=[x, y, z] , size=[length, width, height]  )
        # LOWER LEFTLEG
        # JOINT: Leftleg - LowerLeftleg (rel)
        x, y, z = -1, 0, 0
        pyrosim.Send_Joint( name = "Leftleg_LowerLeftleg" , parent= "Leftleg" , child = "LowerLeftleg" , type = "revolute", position = [x, y, z], jointAxis = "0 1 0")
        # LINK: LowerLeftleg (rel)
        length, width, height = 0.2, 0.2, 1
        x, y, z = 0, 0, -0.5
        pyrosim.Send_Cube(name="LowerLeftleg", pos=[x, y, z] , size=[length, width, height]  )
        
        ## RIGHTLEG
        # JOINT: TORSO - RightLeg (abs)
        x, y, z = baseX + 0.5,baseY +  0, baseZ + 1
        pyrosim.Send_Joint( name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = [x, y, z], jointAxis = "0 1 0")
        # LINK: RightLeg (rel)
        length, width, height = 1, 0.2, 0.2  # SIZE
        x, y, z = 0.5, 0, 0  # POSITION
        pyrosim.Send_Cube(name="Rightleg", pos=[x, y, z] , size=[length, width, height]  )
         # LOWER RIGHTLEG
        # JOINT: Rightleg - LowerRightleg (rel)
        x, y, z = 1, 0, 0
        pyrosim.Send_Joint( name = "Rightleg_LowerRightleg" , parent= "Rightleg" , child = "LowerRightleg" , type = "revolute", position = [x, y, z], jointAxis = "0 1 0")
        # LINK: LowerRightleg (rel)
        length, width, height = 0.2, 0.2, 1
        x, y, z = 0, 0, -0.5
        pyrosim.Send_Cube(name="LowerRightleg", pos=[x, y, z] , size=[length, width, height]  )

        pyrosim.End()

    def Generate_Brain(self, index):
        pyrosim.Start_NeuralNetwork("brain_b" + str(index) + "v"+ str(self.myID) + ".nndf")
        
        linkNames = ["Torso", "Backleg", "Frontleg", "Leftleg", "Rightleg", "LowerBackleg", "LowerFrontleg", "LowerLeftleg", "LowerRightleg"]
        jointNames = ["Torso_Backleg", "Torso_Frontleg", "Torso_Leftleg", "Torso_Rightleg", "Backleg_LowerBackleg", "Frontleg_LowerFrontleg", "Leftleg_LowerLeftleg", "Rightleg_LowerRightleg"]
        
        links = len(linkNames)
        joints = len(jointNames)

        for i in range(0, joints + links):
            if i < links:
                pyrosim.Send_Sensor_Neuron(name = i , linkName = linkNames[i])
            else:
                pyrosim.Send_Motor_Neuron(name = i , jointName = jointNames[i - links])

        # generate synapses
        # iterate over sensor neurons
        for currentRow in range(0, c.numSensorNeurons):
            # iterate over motor neurons
            for currentColumn in range(0,c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,weight = self.weights[currentRow][currentColumn])
                 
        pyrosim.End()

    def Mutate(self):
        chosenRow = random.randint(0, c.numSensorNeurons - 1)
        chosenColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[chosenRow, chosenColumn] = random.random() * 2 - 1 #might need to change 2 for numMotorNeurons

    def SET_ID(self, myID):
        self.myID = str(myID)

    def GET_FITNESS(self):
        print("\n-------------FITNESS: ",str(self.myID),self.fitness,"\n")