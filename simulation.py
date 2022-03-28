from robot import ROBOT
from world import WORLD
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time as t


class SIMULATION:

    # the constructor
    def __init__(self, directOrGui, solutionID):
        
        self.directOrGui = directOrGui
        self.solutionID = solutionID

        # "blind" mode (p.DIRECT) or "heads-up" mode (p.GUI)
        if directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,c.gravity)

        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)

        
    def Run(self):
        for i in range(0,c.ITERATIONS):
            # print(i)
            p.stepSimulation()
            
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            
            if self.directOrGui == "GUI":
                t.sleep(c.sleepingTime)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

