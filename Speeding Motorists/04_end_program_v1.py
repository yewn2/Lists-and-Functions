"""
End Program version 1
This component takes the list of people and prints them out
"""


def end_program(lst, totl):
    totl_ppl = len(lst)
    print(f"Total fines: {totl_ppl}")
    i = 1
    for names in lst:
        print(f"{i}) Name: {names[0]}       Amount Over Limit: {names[1]}")
        i += 1
    print(f"Total amount of fines: ${totl}")