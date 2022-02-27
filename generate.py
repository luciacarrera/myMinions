import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    # cube is part of the world
    length, width, height = 1, 1, 1
    x,y, z = 0,5, height/2
    pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height]  )

    pyrosim.End()

def Generate_Body():
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

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
    pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()