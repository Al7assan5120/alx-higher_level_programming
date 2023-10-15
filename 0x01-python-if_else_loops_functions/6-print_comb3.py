#!/usr/bin/python3
for a in range(0, 9):
    for j in range(a + 1, 10):
        print("{}{}".format(a, j), end="")
        if a == 8 and j == 9:
            print()
        else:
            print(", ", end="")
