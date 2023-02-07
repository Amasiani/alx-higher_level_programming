#!/usr/bin/python3
"""Inheritance"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance of or
       if the oject is an instance of a class it inherited from
       else false.
    Args:
        obj: An object.
        a_class: A class
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
