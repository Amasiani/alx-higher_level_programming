#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attribute
    for anything but attibute called 'first_name'.
    """

    __slots__ = ["first_name"]
