#!/usr/bin/python3
"""Inherits from BaseGeomatery"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle class using BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a new Rectangle class.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
