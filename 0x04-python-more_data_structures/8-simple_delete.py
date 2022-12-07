#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    sim = str(key)
    if sim in a_dictionary:
        a_dictionary.pop(sim)
    return a_dictionary
