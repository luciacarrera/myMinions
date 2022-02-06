import pybullet_data
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")

# prepares sensors
pyrosim.Prepare_To_Simulate(robotId)

for x in range(0,1001):
    t.sleep(1/60)

    # creates sensor
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    p.stepSimulation()
    print(x)
p.disconnect()

