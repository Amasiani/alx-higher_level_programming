#!/usr/bin/python3
def print__last_digit(number);
    if (number < 0);
        number += -1
    last_digit = number % 10
    print("{:d}".format(last_digit), end="")
    return last_digit
