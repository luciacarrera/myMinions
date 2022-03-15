import os
from hillclimber import HILLCLIMBER

'''
for i in range(0,5):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")'''

hc = HILLCLIMBER()
hc.Show_Best()
hc.Evolve()
hc.Show_Best()