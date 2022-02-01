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

    # this cube is part of the robot
    length, width, height = 1, 1, 1
    x,y, z = 0,0, height/2
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height]  )

    # joint between leg and torso (name should always be Parent_Child)
    pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [0.5, 0, 1])
    
    # Leg
    length, width, height = 1, 1, 1
    x,y, z = 1.0,0,1.5
    pyrosim.Send_Cube(name="Leg", pos=[x, y, z] , size=[length, width, height]  )
    pyrosim.End()


Create_World()
Create_Robot()
