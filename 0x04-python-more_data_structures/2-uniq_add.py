#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni = set(my_list)
    uni_list = list(uni)
    sum = 0
    for i in uni_list:
        sum = i + sum
    return sum
