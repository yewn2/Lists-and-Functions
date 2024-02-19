"""
Staff absence list creator v1
"""


def staff_absence(lst):
    print("Input the Staff Name as '$' to stop.")
    ele = [input("Staff Name: "), int(input("Days Absent: "))]
    while "".join(ele[0:1]) != "$":
        for i in range(0, 2):
            lst.append(ele)
            print()
            ele = [input("Staff Name: "), int(input("Days Absent: "))]
    return lst
