# normal.py
import numpy as np

class normal():

    def __init__(self):
        return None
    
    def sample(self,loc=0.0, scale=1.0, size=10):
        return np.random.normal(loc=loc, scale=scale, size=size)
