import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data


class ROBOT:

    def __init__(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.Id = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.Id)

        self.Prepare_To_Sense()
        '''
        self.motors = {}'''

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)



