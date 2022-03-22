from solution import SOLUTION
import constants as c
import copy
import sys

class PARALLEL_HILLCLIMBER:

    def __init__(self):
        self.nextAvailableID = 0

        self.parents = {}
        self.children = {}

        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.parents[i].SET_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
        print(self.nextAvailableID)


    def Evolve(self):
        #directOrGui = sys.argv[1]
        for i in range(0, c.populationSize):
            self.parents[i].Start_Simulation("GUI") 

        for i in range(0, c.populationSize):
            self.parents[i].Wait_For_Simulation_To_End()
            
        # current Generation loop
        for currentGeneration in range(0,c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate() 
        '''
        self.child.Evaluate("DIRECT")
        print("\n\nFITNESS\nParent:",self.parent.fitness,"Child:", self.child.fitness, "\n")
        self.Select()
        '''
        
    def Spawn(self):
        for i in range(0,c.populationSize):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].SET_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            

    def Mutate(self):
        for i in range(0,c.populationSize)
            self.children[i].Mutate()
    

    def Select(self):
        # if child has better fitness than parent, it dethrones them
        if self.parent.fitness > self.child.fitness :
            self.parent = self.child

    #  re-evaluates the parent with graphics turned on.
    def Show_Best(self):
        self.parent.Evaluate("GUI")