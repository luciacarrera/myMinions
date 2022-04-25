import os
from parallelhc import PARALLEL_HILLCLIMBER

os.system("del brain*.nndf")
os.system("del fitness*.txt")
os.system("del temp*.txt")


phc = PARALLEL_HILLCLIMBER()
phc.Evolve()
phc.Show_Best()



'''
phc.Evolve()
phc.Show_Best()'''
