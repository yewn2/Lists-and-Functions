"""
No Absence v1
This function checks which people were not absent at all during the year
"""


def no_absence(lst):
    zero = []
    for names in lst:
        if names[1] == 0:
            zero.append(names[0])
    zero.sort()
    return zero
