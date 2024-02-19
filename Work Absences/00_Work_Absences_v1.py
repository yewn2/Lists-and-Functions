"""
Work Absences version 1
This is the first version of the base component
No functions except main are written yet
"""


def main():
    staff_list_absent = []
    staff_list_absent = staff_absence(staff_list_absent)
    avg = average_absence(staff_list_absent)
    highest, high_amt = most_absence(staff_list_absent)
    none = no_absence(staff_list_absent)
    above_avg = absence_high_avg(staff_list_absent, avg)
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


def statement_formatter(symbol, statement):
    ...


def integer_checker(question):
    ...


def staff_absence(lst):
    ...


def average_absence(lst):
    ...


def most_absence(lst):
    ...


def no_absence(lst):
    ...


def absence_high_avg(lst):
    ...


# main program
main()
