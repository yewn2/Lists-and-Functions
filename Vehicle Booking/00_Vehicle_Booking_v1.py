"""
Base component version 1
No functions written yet except main
"""


def main():
    car_list = [[1, "Suzuki Van", 2], [2, "Toyota Corolla", 4],
                [3, "Honda CRV", 4], [4, "Suzuki Swift", 4],
                [5, "Mitsubishi Airtrek", 4], [6, "Nissan DC Ute", 4],
                [7, "Toyota Previa", 7], [8, "Toyota Hi Ace", 12],
                [9, "Toyota Hi Ace", 12]]
    book_again = True
    while book_again:
        car_list = book(car_list)
    end_program(car_list)


def int_checker(question):
    ...


def book(lst):
    ...


def end_program(lst):
    ...