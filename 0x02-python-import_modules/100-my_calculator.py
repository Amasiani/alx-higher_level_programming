#!/usr/bin/pythons
if __name__ == "_main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv)
    for str in range(argc):
        if (argc != 4):
            print("Usgae: {:s} <a> <operator> <b>".format(sys.argv[str]))
            exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if (sys.argv[2] == '+'):
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            elif (sys.argv[2] == '_'):
                print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            elif (sys.argv[3] == '*'):
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            elif (sys.argv[4] == '/'):
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
            else:
                print("Unknown oparator. Available operators: +, _, * and /")
                exit(1)
            exit(0)