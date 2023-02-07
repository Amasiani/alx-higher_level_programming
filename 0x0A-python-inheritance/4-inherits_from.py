#!/usr/bin/python3
"""Inheritance"""


def inherits_form(obj, a_class):
    """Returns a True if object is an instance of class that inherited
       (directed or indirectedly) from the speciifed class, else false
    Args:
        obj: An object
        a_class: Class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
