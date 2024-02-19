"""
Average Absence list calculator v1
Calculates the average amount of absences throughout the year
"""


def average_absence(lst):
    total = 0
    staff_num = int(len(lst))
    for names in lst:
        total += names[1]
    average = total / staff_num
    return average
