#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return(0)
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 50, 'M': 1000}
    a = 0
    for k in range(len(roman_string)):
        if k > 0 and roman[roman_string[k]] > roman[roman_string[k-1]]:
            a += roman[roman_string[k]] - 2 * roman[roman_string[k-1]]
        else:
            a += roman[roman_string[k]]
    return(a)
