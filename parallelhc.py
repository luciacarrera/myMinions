from solution import SOLUTION
import constants as c
import copy
import sys

class PARALLEL_HILLCLIMBER:

    def __init__(self):
        self.nextAvailableID = 0

        self.parents = {}

        for i in range(0,c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.parents[i].SET_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
        print(self.nextAvailableID)


    def Evolve(self):
        self.Evaluate(self.parents)
        # current Generation loop
        for currentGeneration in range(0,c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate() 
               
        self.Evaluate(self.children)
        exit()
        
        '''
        print("\n\nFITNESS\nParent:",self.parent.fitness,"Child:", self.child.fitness, "\n")
        self.Select()
        '''
        
    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].SET_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            

    def Mutate(self):
        print("\n::::::::::::::::MUTATE")

        for key in self.parents:
            self.children[key].Mutate()
    

    def Select(self):
        # if child has better fitness than parent, it dethrones them
        if self.parent.fitness > self.child.fitness :
            self.parent = self.child

    #  re-evaluates the parent with graphics turned on.
    def Show_Best(self):
        self.parent.Evaluate("GUI")
    
    def Evaluate(self, solutions):
        #directOrGui = sys.argv[1]
        for key in solutions:
            solutions[key].Start_Simulation("GUI") 

        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()
            
        
        