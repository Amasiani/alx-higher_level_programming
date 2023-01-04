#!/usr/bin/python3
for item in range(9):
    for x in range(1, 10):
        if (x < item or x == item):
            continue
        if (item != 0):
            print("{:d}{:d}".format(item, x), end=", ")
        else:
            print("{:d}{:d}".format(item, x))
