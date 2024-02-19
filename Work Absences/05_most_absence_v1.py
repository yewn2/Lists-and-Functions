"""
Most Absence v1
This function calculates which staff had the most absences in the year
"""


def most_absence(lst):
    biggest = 0
    name = ""
    for names in lst:
        if names[1] > biggest:
            biggest = names[1]
            name = names[0]
    return name, biggest
