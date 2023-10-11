#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    x = a_dictionary.copy()
    x = list(x.values())
    x.sort(reverse=True)
    for i, j in a_dictionary.items():
        if j == x[0]:
            return i
