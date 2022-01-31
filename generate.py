import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    # cube is part of the world
    length, width, height = 1, 1, 1
    x,y, z = 0,5, height/2
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height]  )
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    # this cube is part of the robot
    length, width, height = 1, 1, 1
    x,y, z = 0,0, height/2
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height]  )
    pyrosim.End()


Create_World()
Create_Robot()
print("here")