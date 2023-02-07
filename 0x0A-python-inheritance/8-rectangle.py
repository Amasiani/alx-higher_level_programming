#!/usr/bin/python3
"""Inheritance"""


class Rectangle(BaseGeometry):
    """Rectangle class."""

    def __init__(self, width, length):
        """Initializes a Rectangle class.
        Args:
            width (int): Rectangle width.
            length (int): Rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
