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
        print("---------------\n\n")
        self.physicsClient = p.connect(p.GUI)
        print("---------------\n\n")

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        print("---------------\n\n")

        p.setGravity(0,0,c.gravity)


        self.robot = ROBOT()

        self.world = WORLD()
        print("HERE")
        # prepares sensors

        #pyrosim.Prepare_To_Simulate(self.robot)


        

    def Run(self):
        print("\n\n HHH \n\n")
        for i in range(0,c.ITERATIONS):
            print(i)
            
            t.sleep(c.sleepingTime)
            p.stepSimulation()
'''
            # sin stuff
            posBackLeg = c.amplitudeFL * numpy.sin(c.frequencyFL * i + c.phaseOffsetFL)
            posFrontLeg = c.amplitudeBL * numpy.sin(c.frequencyBL * i + c.phaseOffsetBL)

            # creates sensor for backleg        
            backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
            numpy.save('data/backLegSensorValues.npy',backLegSensorValues)

            # creates a sensor for frontleg
            frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
            numpy.save('data/frontLegSensorValues.npy',frontLegSensorValues)

            # motor backleg
            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = posBackLeg, maxForce = c.force)
            
            # motor frontleg
            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition= posFrontLeg, maxForce = c.force)
            '''


                
