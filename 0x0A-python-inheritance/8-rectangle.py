#!/usr/bin/python3
"""Inherits from BaseGeomatery"""
BaseGeometry = __import__('7-base_geometry').Basegeomatry


class Rectangle(BaseGeometry):
    """Defines a Rectangle class using BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle class.
        Args:
            width (int): Rectangle width.
            height (int): Rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
