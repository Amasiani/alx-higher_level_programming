#!/usr/bin/python3
"""Inheritance"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly
       an instance of the specified classelse False
    Args:
        obj: An object.
        a_class: Class(type).
    """
    if type(obj) is a_class:
        return True
    else:
        return False
