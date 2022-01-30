import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")
length, width, height = 1, 2, 3
x,y,z = 0,0,1.5
pyrosim.Send_Cube(name="Box", pos=[0,0,1.5] , size=[length, width, height])

pyrosim.End()
