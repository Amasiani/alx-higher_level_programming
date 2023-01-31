#!/usr/bin/python3
"""A class that defines a reactngle."""


class Reactangle:
    """This represents a rectangle."""

    def __init__(self, width=0, height=0):
        """"Initializing a new  reactnagle class.
        Args:
            width (int): represents the width of the rectangle.
            height (int): represents the height of the rectangle.
        Raise:
            TypeError: If size is not integer.
            ValueError: If size is les than zero.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width attribute"""
        if not isinstance(value, int):
            raise TypeError("width mustb be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the heigth attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
