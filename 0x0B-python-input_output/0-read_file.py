#!/usr/bin/python3
""" a function that reads a text file"""


def read_file(filename=""):
    """ a functiom that prints contents of a file"""
    with open(filename, mode='r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
