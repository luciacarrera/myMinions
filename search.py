import os
from parallelhc import PARALLEL_HILLCLIMBER

os.system("del brain*.nndf")
os.system("del fitness*.txt")
os.system("del temp*.txt")


phc = PARALLEL_HILLCLIMBER("A")
phc.Evolve()
#phc.Show_Best()

phc = PARALLEL_HILLCLIMBER("B")
phc.Evolve()
#phc.Show_Best()



'''
phc.Evolve()
phc.Show_Best()'''
