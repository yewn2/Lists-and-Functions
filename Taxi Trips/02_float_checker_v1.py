"""
Float checker v1
Copied from last project
"""


def float_checker(question):
    error = "\nSorry, you must enter a number\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)
