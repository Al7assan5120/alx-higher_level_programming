#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ele = 0
    if (my_list):
        try:
            if x == 0:
                x = 1
            for i in range(0, x):
                print("{}".format(my_list[i]), end="")
                ele = ele + 1
        except IndexError:
            print()
            return (ele)
        print()
        return (ele)
