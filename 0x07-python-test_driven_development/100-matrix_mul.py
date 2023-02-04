#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices
    Args:
        m_a (list of lists of int/float): Matrix to be multiplied
        m_b (list of lists of int/float): Matrix to be multiplied
    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        TypeError: If row of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied
    Returns:
        A new list which is the outcome of the multiplication
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for element in m_a:
        if not isinstance(element, list):
            raise TypeError("m_a must be a list of lists")
    for element in m_b:
        if not isinstance(element, list):
            raise TypeError("m_b must be a list of lists")
    
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for element in lists:
            if not type(element) in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for lists in m_b:
        for element in lists:
            if not type(element) in (int, float):
                raise TypeError("m_b should contain only integers and floats")

    length = 0
    for element in m_b:
        if length != 0 and length != len(element):
            raise TypeError("each row of m_b must be of the same size")
        length = len(element)
    length = 0
    for element in m_a:
        if length != 0  and length != len(element):
            raise TypeError("each row in m_a must be of the same size")
        length = len(element)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result1 = []
    idx = 0

    for item in m_a:
        result2 = []
        idx1 = 0
        num = 0
        while (idx1 < len(m_b[0])):
            num += item[idx] * m_b[idx][idx1]
            if idx == len(m_b) - 1:
                idx = 0
                result2 += 1
                result2.append(num)
                num = 0
            else:
                idx += 1
        result1.append(result2)
    return result1
