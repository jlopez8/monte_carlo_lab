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
        # update you will have to figure out a way to do this "inverse" mapping business 
        # with the data so really you have to give me the mapped data, AND THE function style of
        # how you generated that data in the first place.
        # the other option is to just have me give you the antithetic function
        # this latter is more straightforward.
        # the former will present a challenge because you will have to compute an
        # inverse CFD probably, but it is from the outside perspective
        # VERY similar to the way the original mc is done.
        # not only that, but the information is essentially the same. ie I have to tell you
        # how this data is distributed in teh first place so you can build antithetic variate
        # OR I have to give you the function that maps the variate assuming I did it correctly.
        # either way, it's one more piece of information compared to the origninal MC estimator. 
        # this is w
        antithetic_estimator = lambda data: sum(func(data) + func(-1 * data)) / (2 * len(data))
        return antithetic_estimator
