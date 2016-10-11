__author__ = 'student'
import random
import numpy as np
import matplotlib.pyplot as plt

def get_percentile(values, bn):
    step = 100/bn
    res = []
    do = 0
    for o in range (bn):
         res.append(np.percentile(values, do))
         do += step
    res[0] = 0.0
    return res

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
    new_one = idx*step
    if add_random == True:
        new_value = idx*step + random.uniform(idx*step, (idx+1)*step)
    return new_one


def values_equalization(values, percentiles, add_random=False):
    for i in range(len(values)):
        values[i] = value_equalization(values[i], percentiles, add_random)
    return values
