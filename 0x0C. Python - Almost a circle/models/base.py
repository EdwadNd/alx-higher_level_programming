#!/usr/bin/python3
""" base class"""
class base:
    """ base class inplementation"""
    def __init__(self, id=None):
        if id is not None:
            id = id
        else:
            __nb_objects =+1
            id = __nb_objects 
