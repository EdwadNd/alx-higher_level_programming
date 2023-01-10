#!/usr/bin/python3
"""  a function that writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """ a function that writes a string to a text file (UTF8) and returns the number of characters written:"""
    with open(filename, mode="w", encoding="utf-8") as f:
        rite = f.write(text)
        return rite
