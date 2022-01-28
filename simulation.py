import pybullet as p
import time as t
physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for x in range(0,1001):
    t.sleep(1/60)
    p.stepSimulation()
    print(x)
p.disconnect()

