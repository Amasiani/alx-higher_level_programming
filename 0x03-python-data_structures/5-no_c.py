#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c') and (my_string[i] != 'C'):
            string += my_string
    return (string)
