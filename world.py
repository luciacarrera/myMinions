import pybullet_data
import pybullet as p

class WORLD:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        self.worldId = p.loadSDF("world.sdf")
        #self.planeId = p.loadURDF("plane.urdf")
        
