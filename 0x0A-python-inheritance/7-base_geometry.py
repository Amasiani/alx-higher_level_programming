#!/usr/bin/python3
"""Defines a base geometry class BAseGeometry"""


class BaseGeometry:
    """this class represent a base geometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a value as an integer
        Args:
            name (string): Character type.
            Value (int): Value of the character.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
