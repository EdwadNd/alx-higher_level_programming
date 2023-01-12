#!/usr/bin/python3
"""pascal triangle"""

def pascal_triangle(n):
    """ pascal triangle calculation"""
    pasc = []
    if n < 0:
        return pasc
    pasc = [[1]]
    while len(pasc) != n:
        tri = pasc[-1]
        helper = [1]
        for i in range(len(tri) - 1):
            helper.append(tri[i] + tri[i + 1])
        helper.append(1)
        pasc.append(helper)
    return pasc
