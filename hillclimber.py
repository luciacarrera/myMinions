from solution import SOLUTION
import constants as c
import copy
import sys

class HILLCLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        #directOrGui = sys.argv[1]
        self.parent.Evaluate("GUI") 

        # current Generation loop
        for currentGeneration in range(0,c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        print("\n\nFITNESS\nParent:",self.parent.fitness," Parents' Average Fitness:","\nChild:", self.child.fitness, " Childrens' Average Fitness:","\n")
        self.Select()
    
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)


    def Mutate(self):
        self.child.Mutate()
    

    def Select(self):
        # if child has better fitness than parent, it dethrones them
        if self.parent.fitness > self.child.fitness :
            self.parent = self.child

    #  re-evaluates the parent with graphics turned on.
    def Show_Best(self):
        self.parent.Evaluate("GUI")