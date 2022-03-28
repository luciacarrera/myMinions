import pybullet as p
import pybullet_data
class WORLD:

    def __init__(self):
    
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        #self.world = p.loadSDF("world.sdf")
        self.plane = p.loadURDF("plane.urdf")


