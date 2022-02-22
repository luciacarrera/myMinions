from robot import ROBOT
from world import WORLD
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time as t


class SIMULATION:

    # the constructor
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,c.gravity)

        self.world = WORLD()
        self.robot = ROBOT()

        
    def Run(self):
        print("\n\n HHH \n\n")
        for i in range(0,c.ITERATIONS):
            
            t.sleep(c.sleepingTime)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act()

            '''
            # sin stuff
            posFrontLeg = c.amplitudeBL * numpy.sin(c.frequencyBL * i + c.phaseOffsetBL)

            
            # motor backleg
            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = posBackLeg, maxForce = c.force)
            
            # motor frontleg
            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition= posFrontLeg, maxForce = c.force)
            '''

    def __del__(self):
        p.disconnect()