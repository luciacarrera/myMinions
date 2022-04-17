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
        # we have to do this for everysingle member of the swarm
        for key in self.parents:
            parentsAverageFitness, kidsAverageFitness = 0, 0

            # get the average fitness from whole swarm
            for index in range(0, c.swarm):
                # see if average x is better in parents or child
                parentsAverageFitness += self.parents[key].swarmFitness[index]
                kidsAverageFitness += self.children[key].swarmFitness[index]

            # divide by swarm
            parentsAverageFitness = parentsAverageFitness / c.swarm
            kidsAverageFitness = kidsAverageFitness / c.swarm

            if parentsAverageFitness > kidsAverageFitness  :
                self.parents[key] = self.children[key]

    #  re-evaluates the parent with graphics turned on.
    # do it for each robot
    def Show_Best(self):
        best_parent = 0
        lowest_fitness = 1000000

        # show best average swarm
        for key in self.parents:
            totalFitness = 0

            for index in range(0,c.swarm):
                totalFitness += self.parents[key].swarmFitness[index]

            averageFitness = totalFitness / c.swarm

            if averageFitness < lowest_fitness:
                best_parent = key
                lowest_fitness = averageFitness

        self.parents[best_parent].Start_Simulation("GUI")
    
    def Evaluate(self, solutions):
        #directOrGui = sys.argv[1]
        for key in solutions:
            solutions[key].Start_Simulation("DIRECT") 

        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()
            
        
    def Print(self):
        for key in self.parents:
            print("\n\n---------FITNESS\nParent:",self.parents[key].swarmFitness,"\nChild:", self.children[key].swarmFitness, "\n")
