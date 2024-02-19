"""
Work Absences version 3
This is the third version of the base component
Average Absence function and Most Absence function added
"""


def main():
    staff_list_absent = []
    staff_list_absent = staff_absence(staff_list_absent)
    avg = average_absence(staff_list_absent)
    highest, high_amt = most_absence(staff_list_absent)
    none = no_absence(staff_list_absent)
    above_avg = absence_high_avg(staff_list_absent, avg)
    print(statement_formatter("-", f"Average number of days staff "
                                   f"were absent: {avg:.2f}"))
    print(statement_formatter("=", f"Person with most days absent: "
                             f"{highest} with {high_amt} days"))
    print("-"*30)
    print("List of people not absent at all: ")
    print("\n".join(none))
    print("-"*30)
    print("="*30)
    print("List of people absent above average: ")
    print("\n".join(above_avg))
    print("="*30)


def statement_formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def staff_absence(lst):
    print("Input the Staff Name as '$' to stop.")
    ele = [input("Staff Name: "), integer_checker("Days Absent: ")]
    while "".join(ele[0:1]) != "$":
        for i in range(0, 2):
            if "".join(ele[0:1]) == "$":
                break
            lst.append(ele)
            print()
            ele = [input("Staff Name: "), integer_checker("Days Absent: ")]
    return lst


def average_absence(lst):
    total = 0
    staff_num = int(len(lst))
    for names in lst:
        total += names[1]
    average = total / staff_num
    return average


def most_absence(lst):
    biggest = 0
    name = ""
    for names in lst:
        if names[1] > biggest:
            biggest = names[1]
            name = names[0]
    return name, biggest


def no_absence(lst):
    ...


def absence_high_avg(lst, average):
    ...


# main program
main()
