#!/usr/bin/python3
"""Inheritance"""


class MyList(list):
    """MyList class that inherits from list.
    Args:
        list (obj): list class.
    """

    def print_sorted(self):
        """Prints a sorted list of integers."""
        return(print(sorted(self)))
