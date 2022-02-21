from robot import ROBOT
from world import WORLD
import constants as c

class SIMULATION:

    # the constructor
    def __init__(self):
        import pybullet as p
        import pybullet_data
        import pyrosim.pyrosim as pyrosim
        physicsClient = p.connect(p.GUI)

        self.robot = ROBOT()
        self.world = WORLD()

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity)
        # prepares sensors
        pyrosim.Prepare_To_Simulate(self.robot)

        # not sure if above or not


        


        