#!/usr/bin/python3
"""Inheritance"""


class BaseGeometry:
    """Geometry class."""

    def area(self):
        """Raise an exception."""
        raise Exception("area() is not implemented)"

    def integer_validator(self, name, value):
        """Validate value
        Args:
            name (string): Name of value.
            value (int): Value.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an ingeter".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
