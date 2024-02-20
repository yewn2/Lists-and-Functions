"""
Base component version 3
End Program component added
"""


def main():
    speeds = []
    speeds, all_fines = speeder(speeds)
    end_program(speeds, all_fines)


def speeder(lst):
    fine = 0
    total = 0
    print("Input the name of speeder as 'x' to stop.")
    print("# " * 13)
    ele = [input("Enter name of speeder: "),
           num_checker("Enter the amount over speed limit: ")]
    while "".join(ele[0:1]) != "x":
        if ele[1] < 10:
            fine = 30
        elif 10 <= ele[1] <= 14:
            fine = 80
        elif 15 <= ele[1] <= 19:
            fine = 120
        elif 20 <= ele[1] <= 24:
            fine = 170
        elif 25 <= ele[1] <= 29:
            fine = 230
        elif 30 <= ele[1] <= 34:
            fine = 300
        elif 35 <= ele[1] <= 39:
            fine = 400
        elif 40 <= ele[1] <= 44:
            fine = 510
        elif ele[1] >= 45:
            fine = 630
        arrest(ele[0])
        print(f"{ele[0]} to be fined ${fine}")
        print("# " * 13)
        lst.append(ele)
        print()
        print("# " * 13)
        total += fine
        ele = [input("Enter name of speeder: "),
               num_checker("Enter the amount over speed limit: ")]
    return lst, total


def arrest(name):
    name2 = name.lower()
    if (name2 == "james wilson" or name2 == "helga norman"
            or name2 == "zachary conroy"):
        print(f"{name.upper()} - WARRANT TO ARREST")


def num_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def end_program(lst, totl):
    totl_ppl = len(lst)
    print(f"Total fines: {totl_ppl}")
    for names in lst:
        print(f") Name: {names[0]}       Amount Over Limit: {names[1]}")
    print(f"Total amount of fines: ${totl}")


# main program
if __name__ == '__main__':
    main()
