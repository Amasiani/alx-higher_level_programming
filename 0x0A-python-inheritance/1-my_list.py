#!/usr/bin/python3
"""Inheritance"""


class MyList(list):
    """MyList class that inherits from list.
    Args:
        list (obj): list class.
    """

    def print_sorted(self, list1):
        """prints a sorted list
        Args:
            list1 (list): List of integer
        """
        return(print(sorted(list1)))
