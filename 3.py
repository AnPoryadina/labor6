__author__ = 'student'
if __name__=="__main__":

import numpy as np
import random
import matplotlib.pyplot as plt

def get_percentile(values, bn):
    step = 100/bn
    result = []
    act = 0
    for o in range (bn):
         result.append(np.percentile(values, act))
         act += step
    result[0] = 0.0
    return result

def get_percentile_number(value, percentiles):
    i = 0
    while percentiles[i] <= value:
        index = i
        if i <len(percentiles)-1:
            i+=1
        else:
            break
    return index

def value_equalization(value, percentiles, add_random = False):
    idx = get_percentile_number(value, percentiles)
    step = 1/len(percentiles)
    new_value = idx*step
    if add_random == True:
        new_value = idx*step + random.uniform(idx*step, (idx+1)*step)
    return new_value



