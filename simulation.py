import pybullet_data
import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

p.loadSDF("box.sdf")

for x in range(0,1001):
    t.sleep(1/60)
    p.stepSimulation()
    print(x)
p.disconnect()

