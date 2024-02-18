"""
Staff absence list creator v1
"""


def staff_absence(lst, amount):
    staff = "x"
    while staff != "$":
        staff, days = input("\nEnter the staff name and the number of days "
                            "absent, separated by a comma and space.\n"
                            "Enter the staff name as '$' and the days "
                            "as '0' to finish. ").split(", ")
        lst.append(staff)
        amount.append(days)
    return lst, amount
