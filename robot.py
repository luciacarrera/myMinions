import pybullet_data
import pybullet as p

class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        self.sensors = ()
        self.motor = ()
