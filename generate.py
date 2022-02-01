import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    # cube is part of the world
    length, width, height = 1, 1, 1
    x,y, z = 0,5, height/2
    pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height]  )

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    # LINK: TORSO (abs)
    length, width, height = 1, 1, 1
    x,y, z = 0, 0, 1+height/2
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height]  )

    # JOINT: TORSO - BACKLEG (abs)
    x, y, z = 0.5, 0, 1
    pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [x,y,z])
    
    # LINK: BACKLEG (rel)
    length, width, height = 1, 1, 1
    x,y, z = 0.5,0,-0.5
    pyrosim.Send_Cube(name="Backleg", pos=[x, y, z] , size=[length, width, height]  )
    
    # JOINT: TORSO - FRONTLEG (abs)
    x, y, z = -0.5, 0, 1
    pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [x, y, z])

    # LINK: FRONTLEG (rel)
    length, width, height = 1, 1, 1
    x,y, z = -0.5,0,-0.5
    pyrosim.Send_Cube(name="Frontleg", pos=[x, y, z] , size=[length, width, height]  )
    
    pyrosim.End()


Create_World()
Create_Robot()
