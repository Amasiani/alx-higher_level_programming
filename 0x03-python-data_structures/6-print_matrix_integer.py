#!/usr/bin/python3
def print_matrix_integer(matrox=[[]]):
    for x in matrix:
        s = ""
        for y in x:
            print("{:s}{:d}".format(s, y, end=''))
            s = " "
        print()
