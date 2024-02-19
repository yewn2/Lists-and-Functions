"""
Absence Higher than Average v1
This function checks which staff were absent more than the average
"""


def absence_high_avg(lst, average):
    lofty = []
    for names in lst:
        if names[1] > average:
            lofty.append("".join(str(names)))
    lofty.sort()
    return lofty
