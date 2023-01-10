#!/usr/bin/python3
""" student class"""


class Student:
    """ student class
    """

    def __init__(self, first_name, last_name, age):
        """ Args:
            first_name (str): first name of the student
            second_name (str): second name of the student.
            age (int): age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary method.
        """
        if attrs is not None:
            listLatt = [x for x in attrs if x in list(self.__dict__.keys())]
            try:
                return self.__dict__[listLatt]
            except KeyError:
                return self.__dict__
        else:
            return self.__dict__
