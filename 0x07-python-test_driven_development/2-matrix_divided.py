#!/usr/bin/python3
"""
decribes a divide Function
"""


def matrix_divided(matrix, div):
    """
    Function That Divides All Elementes of a Matrix
    """
    if isinstance(matrix, list) or len(matrix) < 1:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix[0], list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    len_matrix = len(matrix[0])
    new_list = []

    for count, i in enumerate(matrix):
        if isinstance(i, list) or len(i) < 1:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if len(i) != len_matrix:
            raise TypeError("Each row of the matrix must have the same size")

        new_list.append([])
        for j in i:
            if isinstance(j, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            new_list[count].append(round(j / div, 2))
    return new_list
