#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # I can convert a dictionary into a list with the following code
    #
    # print(a_dictionary)
    # dict_list = list(a_dictionaru.items())
    # print(dict_list)
    #
    for i, j in sorted(a_dictionary.items()):
        print("{}: {}".format(i, j))
