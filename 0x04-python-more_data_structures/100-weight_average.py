#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum1 = 0
    den = 0
    for i in my_list:
        sum1 = i[0] * i[1] + sum1
        den = i[1] + den
    return sum1 / den
