from solution import SOLUTION
import constants as c
import copy
import sys

class PARALLEL_HILLCLIMBER:

    def __init__(self):
        self.nextAvailableID = 0

        self.parents = {}
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        print(self.nextAvailableID)


    def Evolve(self):
        #directOrGui = sys.argv[1]
        for i in range(0, c.populationSize):
            self.parents[i].Evaluate("GUI") 

    '''
        # current Generation loop
        for currentGeneration in range(0,c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        print("\n\nFITNESS\nParent:",self.parent.fitness,"Child:", self.child.fitness, "\n")
        self.Select()
    
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        # set id
        # +1 to next id


    def Mutate(self):
        self.child.Mutate()
    

    def Select(self):
        # if child has better fitness than parent, it dethrones them
        if self.parent.fitness > self.child.fitness :
            self.parent = self.child

    #  re-evaluates the parent with graphics turned on.
    def Show_Best(self):
        self.parent.Evaluate("GUI")'''