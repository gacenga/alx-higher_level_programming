#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weightedsum = sum(score * weight for score, weight in my_list)
    weight = sum(weight for _, weight in my_list)
    if weightedsum != 0:
        return weightedsum / weight
    else:
        return 0
