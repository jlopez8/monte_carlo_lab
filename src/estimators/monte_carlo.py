# monte_carlo.py

import numpy as np

class build_estimator():
    def build_estimator(self, func, **params): 
        mc_estimator = lambda data: sum(func(data)) / len(data)
        return mc_estimator
    