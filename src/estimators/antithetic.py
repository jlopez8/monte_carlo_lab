# antithetic.py

import numpy as np

class antithetic():
    def __init__(self):
        return None
    
    def estimator(self, func):
        """
        You have to make an assumption on the data you are 
        applying to this function in the antithetic variate.
        Let us assume you can simply apply a negative.
        """
        # data_p = -1 * data
        antithetic_estimator = lambda data: sum(func(data) + func(-1 * data)) / (2 * len(data))
        return antithetic_estimator
