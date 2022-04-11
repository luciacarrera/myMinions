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
            print(self.nextAvailableID)
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
        self.Print()
        #exit()
        self.Select()
    
        
    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].SET_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            

    def Mutate(self):
        for key in self.parents:
            self.children[key].Mutate()
    

    def Select(self):
        # if child has better fitness than parent, it dethrones them
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness :
                self.parents[key] = self.children[key]

    #  re-evaluates the parent with graphics turned on.
    def Show_Best(self):
        best_parent = 0
        lowest_fitness = 1000000
        for key in self.parents:
            if self.parents[key].fitness < lowest_fitness:
                best_parent = key
                lowest_fitness = self.parents[key].fitness 

        self.parents[best_parent].Start_Simulation("GUI")
    
    def Evaluate(self, solutions):
        #directOrGui = sys.argv[1]
        for key in solutions:
            solutions[key].Start_Simulation("DIRECT") 

        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()
            
        
    def Print(self):
        for key in self.parents:
            print("\n\n---------FITNESS\nParent:",self.parents[key].fitness,"Child:", self.children[key].fitness, "\n")
