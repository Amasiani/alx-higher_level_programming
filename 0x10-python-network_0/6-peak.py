#!/usr/bin/python3
"""
*Function that finds a peak in a list of unsorted integers.
*Prototype: def find_peak(list_of_integers):
*You are not allowed to import any module
*Algorithm must have the lowest complexity (hint:
 you don’t need to go through all numbers to find a peak)
*6-peak.py must contain the function
*6-peak.txt must contain the complexity of your algorithm:
 O(log(n)), O(n), O(nlog(n)) or O(n2)
*Note: there may be more than one peak in the list
"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
