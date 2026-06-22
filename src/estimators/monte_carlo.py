# monte_carlo.py

import numpy as np

class monte_carlo():
    def __init__(self):
        return None
    
    def estimator(self, func, **params): 
        mc_estimator = lambda data: sum(func(data)) / len(data)
        return mc_estimator
    