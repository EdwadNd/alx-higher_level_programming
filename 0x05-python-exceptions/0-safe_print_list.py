#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    word = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            word += 1
        except:
            continue
    print()
    return word