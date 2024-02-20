"""
Speeding arrest version 1
Asks for the name, amount over limit and calculates the fine
"""


def speeder(lst):
    fine = 0
    print("Input the name of speeder as 'x' to stop.")
    print("# " * 13)
    ele = [input("Enter name of speeder: "),
           int(input("Enter the amount over speed limit: "))]
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
        print(f"{ele[0]} to be fined ${fine}")
        print("# " * 13)
        lst.append(ele)
        print()
        print("# " * 13)
        ele = [input("Enter name of speeder: "),
               int(input("Enter the amount over speed limit: "))]
    return lst
