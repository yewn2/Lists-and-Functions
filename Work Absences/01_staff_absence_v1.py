"""
Staff absence list creator v1
"""


def staff_absence(lst, amount):
    staff, days = input("\nEnter the staff name and the number of days "
                        "absent, separated by a comma and space.\n"
                        "Enter the staff name as '$' and the days "
                        "as '0' to finish. ").split(", ")
    while staff != "$":
        lst.append(staff)
        amount.append(days)
        staff, days = input("\nEnter the staff name and the number of days "
                            "absent, separated by a comma and space.\n"
                            "Enter the staff name as '$' and the days "
                            "as '0' to finish. ").split(", ")
    return lst, amount
