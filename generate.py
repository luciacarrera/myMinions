import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")


length, width, height = 1, 1, 1
x,y,z = 0,0, height/2
# creates cols
for i in range(0,5):
        
    # creates row
    for j in range(0,5):
        
        # creates tower
        for k in range(0,10):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
            z = z + height 
            width = 0.9 * width
            height = 0.9 * height
            length = 0.9 * length

        length, width, height = 1, 1, 1
        x,y,z = x,y, height/2
        x = x + length

    x = 0
    y = y + width


pyrosim.End()
