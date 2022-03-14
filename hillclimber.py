from solution import SOLUTION
import constants as c
import copy

class HILLCLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate() 

        # current Generation loop
        #for currentGeneration in c.numberOfGenerations:
        self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Select()
    
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)


    def Mutate(self):
        self.child.Mutate()
    

    def Select(self):
        # if child has better fitness than parent, it dethrones them
        if self.parent.fitness < self.child.fitness :
            self.parent.fitness = self.child.fitness