"""
Work Absences version 2
This is the second version of the base component
Staff absence list creator function added
"""


def main():
    staff_list = []
    days_absent = []
    staff_list, days_absent = staff_absence(staff_list, days_absent)
    avg = average_absence(staff_list, days_absent)
    highest, high_amt = most_absence(staff_list, days_absent)
    none = no_absence(staff_list, days_absent)
    above_avg = absence_high_avg(staff_list, days_absent, avg)
    statement_formatter("-", f"Average number of days staff were absent: "
                             f"{avg:.2f}")
    statement_formatter("=", f"Person with most days absent: "
                             f"{highest} with {high_amt}")
    print("-"*30)
    print("List of people not absent at all: ")
    print("\n".join(none))
    print("-"*30)
    print("="*30)
    print("List of people absent above average: ")
    print("\n".join(above_avg))
    print("="*30)


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


def average_absence(lst, amount):
    ...


def most_absence(lst, amount):
    ...


def no_absence(lst, amount):
    ...


def absence_high_avg(lst, amount):
    ...


def statement_formatter(symbol, statement):
    ...
