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

    # this cube is part of the robot (Link 0) - uses abs coordinates
    length, width, height = 1, 1, 1
    x,y, z = 0,0, height/2
    pyrosim.Send_Cube(name="Link0", pos=[x, y, z] , size=[length, width, height]  )

    # joint between leg and torso (name should always be Parent_Child) - uses absolute coordinates
    x, y, z = 0, 0, 1
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [x,y,z])
    
    # Leg (second link) Link 1# joint between leg and torso (name should always be Parent_Child) 
    length, width, height = 1, 1, 1
    x,y, z = 0,0,0.5
    pyrosim.Send_Cube(name="Link1", pos=[x, y, z] , size=[length, width, height]  )
    
    # second joint - relative coordinates
    x, y, z = 0,0,1
    pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [x, y, z])

    # third link - relative coordinates
    length, width, height = 1, 1, 1
    x,y, z = 0,0,0.5
    pyrosim.Send_Cube(name="Link2", pos=[x, y, z] , size=[length, width, height]  )

    # third joint - relative coordinates
    x, y, z = 0,0.5,0.5
    pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [x, y, z])

    # fourth link - relative coordinates
    length, width, height = 1, 1, 1
    x,y, z = 0,0.5,0
    pyrosim.Send_Cube(name="Link3", pos=[x, y, z] , size=[length, width, height]  )

    pyrosim.End()


Create_World()
Create_Robot()
