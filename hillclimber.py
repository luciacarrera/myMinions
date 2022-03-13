from solution import SOLUTION
import constants as c

class HILLCLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate() 

        # current Generation loop
        for currentGeneration in c.numberOfGenerations:
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Select()
    
    def Spawn(self):
        pass
    

    def Mutate(self):
        pass

    def Select(self):
        pass