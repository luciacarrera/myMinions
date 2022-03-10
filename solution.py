import numpy

class SOLUTION:

    def __init__(self):
        ROWS = 3
        COLUMNS = 2
        self.weights =  numpy.random.rand(ROWS,COLUMNS)
        self.weights = self.weights * 2 - 1

