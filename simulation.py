from robot import ROBOT
from world import WORLD
import constants as c

# connect to pybullet
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self):
        # create world and robot
        self.world = WORLD()
        self.robot = ROBOT()

        # set additional search path
        self.path = p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # set gravity
        self.gravity = p.setGravity(0,0, c.GRAVITY)

        # prepare to simulate
        self.pyrosim.Prepare_To_Simulate(self.robotId)

        
    
    def Run(self):
        for i in range(0,c.ITERATIONS):
            print(i)
    '''    t.sleep(1/60.0)
        p.stepSimulation()

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
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Backleg", controlMode = p.POSITION_CONTROL, targetPosition = posBackLeg, maxForce = c.maxForce)
        
        # motor frontleg
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_Frontleg", controlMode = p.POSITION_CONTROL, targetPosition= posFrontLeg, maxForce = c.maxForce)
'''