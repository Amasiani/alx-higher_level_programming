#!/usr/bin/python3
for item in range(100):
    if (item != 99):
        print("{:02d}".format(item), end=", ")
    else:
        print("{:02d}".format(item))
